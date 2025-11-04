# Complete Setup Guide for Windows 11 RDP

This comprehensive guide will walk you through setting up your free Windows 11 RDP environment step by step.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Repository Setup](#repository-setup)
3. [Ngrok Configuration](#ngrok-configuration)
4. [GitHub Secrets Configuration](#github-secrets-configuration)
5. [Running the Workflow](#running-the-workflow)
6. [Connecting from Different Devices](#connecting-from-different-devices)
7. [Troubleshooting](#troubleshooting)

## Prerequisites

- A GitHub account (free)
- An ngrok account (free)
- An RDP client application on your device

## Repository Setup

### Step 1: Fork the Repository
1. Go to the main repository page
2. Click the **Fork** button in the top-right corner
3. Select your account as the destination
4. Click **Create fork**

### Step 2: Enable GitHub Actions
1. Go to your forked repository
2. Click the **Actions** tab
3. If prompted, click **I understand my workflows, go ahead and enable them**

## Ngrok Configuration

### Step 1: Create Ngrok Account
1. Visit [ngrok.com](https://ngrok.com/)
2. Click **Sign up** and create a free account
3. Verify your email address

### Step 2: Get Authentication Token
1. After logging in, go to [Your Authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)
2. Copy the authentication token (it looks like: `2abc123def456ghi789jkl0mn`)
3. **Keep this token secure** - treat it like a password

## GitHub Secrets Configuration

### Step 1: Access Repository Settings
1. Go to your forked repository on GitHub
2. Click the **Settings** tab (next to the Pull requests tab)
3. In the left sidebar, find **Security** section
4. Click **Secrets and variables**
5. Click **Actions**

### Step 2: Add Ngrok Token
1. Click **New repository secret**
2. Name: `NGROK_AUTH_TOKEN`
3. Secret: Paste your ngrok authentication token
4. Click **Add secret**

## Running the Workflow

### Step 1: Navigate to Actions
1. Go to your repository
2. Click the **Actions** tab
3. You should see "Windows 11 RDP" workflow

### Step 2: Run the Workflow
1. Click on **Windows 11 RDP** workflow
2. Click **Run workflow** button (on the right side)
3. You can optionally change the password (default is `P@ssw0rd123!`)
4. Click **Run workflow**

### Step 3: Monitor Progress
1. The workflow will start running (green dot appears)
2. Click on the running workflow to see live logs
3. Wait for the "Start Ngrok Tunnel" step to complete
4. Look for connection details in the logs

## Connecting from Different Devices

### Windows Desktop
1. Open **Remote Desktop Connection**
2. Computer: Enter the ngrok URL (without `tcp://`)
3. Username: `runneradmin`
4. Password: Your set password
5. Click **Connect**

### Mac
1. Download **Microsoft Remote Desktop** from Mac App Store
2. Click **+** to add new connection
3. PC name: Enter ngrok URL
4. User account: `runneradmin` with your password
5. Click **Connect**

### Linux
1. Install Remmina: `sudo apt install remmina`
2. Open Remmina
3. Protocol: RDP
4. Server: Enter ngrok URL
5. Username: `runneradmin`
6. Password: Your password
7. Click **Connect**

### Android Phone/Tablet
1. Install **Microsoft Remote Desktop** from Google Play
2. Tap **+** to add connection
3. PC name: Enter ngrok URL
4. User name: `runneradmin`
5. Password: Your password
6. Tap **Save** then **Connect**

### iPhone/iPad
1. Install **Microsoft Remote Desktop** from App Store
2. Tap **+** and select **Desktop**
3. PC name: Enter ngrok URL
4. User account: Add `runneradmin` with password
5. Tap **Save** then **Connect**

## Understanding the Connection URL

When you check the workflow logs, you'll see something like:
```
Tunnel URL: tcp://4.tcp.ngrok.io:12345
```

**For RDP clients, use:** `4.tcp.ngrok.io:12345` (remove the `tcp://` part)

## Session Management

### Session Duration
- Default: 6 hours maximum
- You can cancel and restart to reset the timer
- The session will automatically end after 6 hours

### Multiple Sessions
- You can run multiple workflows simultaneously
- Each gets a unique ngrok URL
- Be mindful of ngrok's free tier limits

### Stopping a Session
1. Go to **Actions** tab
2. Click on the running workflow
3. Click **Cancel workflow**

## Troubleshooting

### Common Issues and Solutions

#### "Authentication failed" Error
**Problem:** Ngrok authentication fails
**Solution:**
- Double-check your `NGROK_AUTH_TOKEN` in repository secrets
- Ensure the token is copied correctly (no extra spaces)
- Verify your ngrok account is active

#### "Cannot connect to RDP"
**Problem:** RDP client can't connect
**Solutions:**
- Ensure workflow completed successfully
- Check you're using the correct URL format (without `tcp://`)
- Verify credentials: `runneradmin` and your password
- Try a different RDP client
- Check if your firewall is blocking the connection

#### "Workflow doesn't start"
**Problem:** The workflow fails to run
**Solutions:**
- Ensure GitHub Actions is enabled in your repository
- Check if the workflow file exists in `.github/workflows/`
- Verify you have the correct permissions

#### "Ngrok tunnel not created"
**Problem:** Ngrok fails to create tunnel
**Solutions:**
- Check if you've exceeded ngrok's free tier limits
- Verify your ngrok account is in good standing
- Try running the workflow again

#### Mobile Connection Issues
**Problem:** Can't connect from mobile device
**Solutions:**
- Ensure you're using the mobile app, not web browser
- Check your mobile internet connection
- Try switching between WiFi and mobile data
- Verify the URL format is correct
- Restart the mobile RDP app

### Getting Additional Help
- Check the repository's [Issues](../../issues) page
- Review workflow logs for specific error messages
- Consult ngrok documentation for tunneling issues
- Join GitHub Discussions for community support

## Security Best Practices

1. **Use Strong Passwords**: Always set a custom, strong password
2. **Monitor Access**: Keep track of who has access to your repository
3. **Limit Session Time**: Don't leave sessions running unnecessarily
4. **Secure Networks**: Avoid using on public WiFi without VPN
5. **Regular Cleanup**: Don't store sensitive data on the RDP session

## Performance Optimization

### For Desktop Clients
- Adjust color depth to 16-bit for better performance
- Disable desktop composition
- Reduce audio quality if not needed

### For Mobile Clients
- Use "Fit to screen" mode
- Enable touch mode if available
- Consider using external keyboard/mouse for extended use

---

**Need more help?** Open an issue in the repository or check the main README for additional information.