#!/usr/bin/env python3
"""
GitHub OAuth Integration Module

Handles GitHub OAuth authentication flow for the Windows 11 RDP Manager.
Provides secure token management and API access.

Author: Windows 11 RDP Project
License: MIT
"""

import json
import requests
import secrets
import webbrowser
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
import time
from typing import Optional, Dict, Any


class GitHubOAuthHandler(BaseHTTPRequestHandler):
    """HTTP handler for OAuth callback"""
    
    def do_GET(self):
        """Handle GET request for OAuth callback"""
        # Parse URL and query parameters
        url_parts = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(url_parts.query)
        
        # Check for authorization code
        if 'code' in query_params:
            auth_code = query_params['code'][0]
            self.server.auth_code = auth_code
            
            # Send success response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            success_html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Authentication Successful</title>
                <style>
                    body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background: #f0f8ff; }
                    .success { color: #2e7d32; font-size: 24px; margin: 20px 0; }
                    .instruction { color: #424242; font-size: 16px; margin: 20px 0; }
                    .close-btn { background: #1976d2; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
                </style>
            </head>
            <body>
                <h1>✓ Authentication Successful!</h1>
                <div class="success">GitHub OAuth completed successfully.</div>
                <div class="instruction">You can now close this window and return to the RDP Manager.</div>
                <button class="close-btn" onclick="window.close()">Close Window</button>
            </body>
            </html>
            """
            
            self.wfile.write(success_html.encode())
            
        elif 'error' in query_params:
            error = query_params['error'][0]
            error_description = query_params.get('error_description', [''])[0]
            
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            error_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Authentication Error</title>
                <style>
                    body {{ font-family: Arial, sans-serif; text-align: center; padding: 50px; background: #fff3e0; }}
                    .error {{ color: #d32f2f; font-size: 24px; margin: 20px 0; }}
                    .description {{ color: #424242; font-size: 16px; margin: 20px 0; }}
                </style>
            </head>
            <body>
                <h1>❌ Authentication Error</h1>
                <div class="error">Error: {error}</div>
                <div class="description">{error_description}</div>
                <p>Please close this window and try again.</p>
            </body>
            </html>
            """
            
            self.wfile.write(error_html.encode())
        
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Invalid callback request')
    
    def log_message(self, format, *args):
        """Suppress default logging"""
        pass


class GitHubAuth:
    """GitHub OAuth authentication manager"""
    
    def __init__(self, client_id: str = None, client_secret: str = None):
        """
        Initialize GitHub OAuth manager
        
        Note: For security, client_id and client_secret should be loaded from
        environment variables or secure configuration in production.
        """
        # GitHub OAuth App credentials (these would be registered with GitHub)
        # For this demo, using placeholder values
        self.client_id = client_id or "your_github_client_id"
        self.client_secret = client_secret or "your_github_client_secret"
        
        # OAuth configuration
        self.redirect_uri = "http://localhost:8080/callback"
        self.scope = "repo,workflow"  # Required scopes for RDP management
        
        # Runtime state
        self.access_token: Optional[str] = None
        self.user_info: Optional[Dict[str, Any]] = None
        self.callback_server: Optional[HTTPServer] = None
    
    def start_oauth_flow(self) -> str:
        """
        Start the OAuth authorization flow
        
        Returns:
            Authorization URL that user should visit
        """
        # Generate state parameter for security
        state = secrets.token_urlsafe(32)
        
        # Build authorization URL
        auth_params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'scope': self.scope,
            'state': state,
            'allow_signup': 'true'
        }
        
        auth_url = "https://github.com/login/oauth/authorize?" + urllib.parse.urlencode(auth_params)
        
        # Start local callback server
        self._start_callback_server()
        
        return auth_url
    
    def _start_callback_server(self):
        """Start local HTTP server to handle OAuth callback"""
        try:
            self.callback_server = HTTPServer(('localhost', 8080), GitHubOAuthHandler)
            self.callback_server.auth_code = None
            
            # Run server in background thread
            server_thread = Thread(target=self._run_callback_server, daemon=True)
            server_thread.start()
            
        except OSError as e:
            raise Exception(f"Failed to start callback server: {e}")
    
    def _run_callback_server(self):
        """Run the callback server"""
        try:
            self.callback_server.serve_forever()
        except Exception:
            pass  # Server was shutdown
    
    def wait_for_callback(self, timeout: int = 300) -> Optional[str]:
        """
        Wait for OAuth callback with authorization code
        
        Args:
            timeout: Maximum time to wait in seconds
        
        Returns:
            Authorization code if received, None if timeout
        """
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            if self.callback_server and hasattr(self.callback_server, 'auth_code'):
                if self.callback_server.auth_code:
                    auth_code = self.callback_server.auth_code
                    self._stop_callback_server()
                    return auth_code
            
            time.sleep(0.5)
        
        self._stop_callback_server()
        return None
    
    def _stop_callback_server(self):
        """Stop the callback server"""
        if self.callback_server:
            self.callback_server.shutdown()
            self.callback_server = None
    
    def exchange_code_for_token(self, auth_code: str) -> bool:
        """
        Exchange authorization code for access token
        
        Args:
            auth_code: Authorization code from callback
        
        Returns:
            True if successful, False otherwise
        """
        token_data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': auth_code,
            'redirect_uri': self.redirect_uri
        }
        
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'Windows-11-RDP-Manager/1.0'
        }
        
        try:
            response = requests.post(
                'https://github.com/login/oauth/access_token',
                data=token_data,
                headers=headers,
                timeout=30
            )
            
            if response.status_code == 200:
                token_info = response.json()
                
                if 'access_token' in token_info:
                    self.access_token = token_info['access_token']
                    return True
                else:
                    print(f"Token exchange error: {token_info}")
                    return False
            else:
                print(f"HTTP error during token exchange: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"Exception during token exchange: {e}")
            return False
    
    def get_user_info(self) -> Optional[Dict[str, Any]]:
        """
        Get authenticated user information
        
        Returns:
            User info dictionary or None if failed
        """
        if not self.access_token:
            return None
        
        headers = {
            'Authorization': f'token {self.access_token}',
            'Accept': 'application/json',
            'User-Agent': 'Windows-11-RDP-Manager/1.0'
        }
        
        try:
            response = requests.get(
                'https://api.github.com/user',
                headers=headers,
                timeout=30
            )
            
            if response.status_code == 200:
                self.user_info = response.json()
                return self.user_info
            else:
                return None
                
        except Exception:
            return None
    
    def trigger_workflow(self, owner: str, repo: str, workflow_file: str, 
                        inputs: Dict[str, str] = None) -> bool:
        """
        Trigger a GitHub Actions workflow
        
        Args:
            owner: Repository owner
            repo: Repository name
            workflow_file: Workflow file name (e.g., 'tailscale-rdp.yml')
            inputs: Workflow input parameters
        
        Returns:
            True if successful, False otherwise
        """
        if not self.access_token:
            return False
        
        headers = {
            'Authorization': f'token {self.access_token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Windows-11-RDP-Manager/1.0'
        }
        
        # Workflow dispatch payload
        payload = {
            'ref': 'main',
            'inputs': inputs or {}
        }
        
        url = f'https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_file}/dispatches'
        
        try:
            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=30
            )
            
            return response.status_code == 204  # GitHub returns 204 for successful dispatch
            
        except Exception as e:
            print(f"Error triggering workflow: {e}")
            return False
    
    def get_workflow_runs(self, owner: str, repo: str) -> Optional[list]:
        """
        Get recent workflow runs for a repository
        
        Args:
            owner: Repository owner
            repo: Repository name
        
        Returns:
            List of workflow runs or None if failed
        """
        if not self.access_token:
            return None
        
        headers = {
            'Authorization': f'token {self.access_token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Windows-11-RDP-Manager/1.0'
        }
        
        url = f'https://api.github.com/repos/{owner}/{repo}/actions/runs'
        
        try:
            response = requests.get(
                url,
                headers=headers,
                params={'per_page': 10},  # Get last 10 runs
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json().get('workflow_runs', [])
            else:
                return None
                
        except Exception:
            return None
    
    def is_authenticated(self) -> bool:
        """Check if user is authenticated"""
        return self.access_token is not None
    
    def logout(self):
        """Clear authentication state"""
        self.access_token = None
        self.user_info = None
        self._stop_callback_server()


# Demo usage
if __name__ == '__main__':
    # This is for testing purposes only
    auth = GitHubAuth()
    
    print("Starting GitHub OAuth flow...")
    auth_url = auth.start_oauth_flow()
    print(f"Visit: {auth_url}")
    
    print("Waiting for callback...")
    auth_code = auth.wait_for_callback()
    
    if auth_code:
        print("Received authorization code, exchanging for token...")
        if auth.exchange_code_for_token(auth_code):
            user_info = auth.get_user_info()
            if user_info:
                print(f"Authenticated as: {user_info['login']}")
            else:
                print("Failed to get user info")
        else:
            print("Failed to exchange code for token")
    else:
        print("No authorization code received (timeout or error)")