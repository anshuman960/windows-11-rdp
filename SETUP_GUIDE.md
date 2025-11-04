# Complete Setup Guide for Windows 11 RDP Manager

This comprehensive guide will walk you through setting up your Windows 11 RDP environment using the new Tailscale-powered desktop application.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Download and Install](#download-and-install)
3. [Account Setup](#account-setup)
4. [Desktop Application Setup](#desktop-application-setup)
5. [First RDP Session](#first-rdp-session)
6. [Connecting from Different Devices](#connecting-from-different-devices)
7. [Troubleshooting](#troubleshooting)

## Prerequisites

- **Windows System**: Windows 7 or later (x86 or x64)
- **Internet Connection**: Stable internet for GitHub and Tailscale
- **GitHub Account**: Free GitHub account
- **Tailscale Account**: Free Tailscale account (no credit card required)

## Download and Install

### Step 1: Download the Desktop Application
1. Go to the [Releases page](https://github.com/anshuman960/windows-11-rdp/releases)
2. Download the appropriate version:
   - **`Windows11-RDP-Manager-x64.exe`** - For 64-bit Windows (recommended)
   - **`Windows11-RDP-Manager-x86.exe`** - For 32-bit Windows
3. Or download the portable ZIP package if you prefer

### Step 2: Run the Application
1. **Extract** the ZIP file if you downloaded the portable version
2. **Run** `Windows11-RDP-Manager-[architecture].exe`
3. Windows may show a security warning - click **"More info"** then **"Run anyway"**
4. The application will start and show the main interface

## Account Setup

### Step 1: Create GitHub Account (if needed)
1. Visit [github.com](https://github.com/)
2. Click **"Sign up"** and create a free account
3. **Verify your email** address
4. **Fork** the [windows-11-rdp repository](https://github.com/anshuman960/windows-11-rdp) to your account

### Step 2: Create Tailscale Account
1. Visit [tailscale.com](https://tailscale.com/)
2. Click **"Start connecting devices"**
3. **Sign up with GitHub** (recommended for easy integration)
4. **No credit card required** - the free tier covers personal use
5. Complete the account verification if prompted

### Step 3: Generate Tailscale Auth Key
1. In your Tailscale dashboard, go to **Settings** → **Keys**
2. Click **"Generate auth key"**
3. **Settings to use**:
   - **Ephemeral**: ✅ Enabled (recommended)
   - **Pre-authorized**: ✅ Enabled
   - **Expires**: 90 days (or your preference)
   - **Tags**: Leave empty or use `tag:rdp`
4. Click **"Generate key"**
5. **Copy the key** - it starts with `tskey-auth-...`
6. **⚠️ Important**: Save this key securely - you won't see it again!

## Desktop Application Setup

### Step 1: GitHub Authentication
1. Open the **Windows 11 RDP Manager**
2. Go to the **"Authentication"** tab
3. Click **"Authenticate with GitHub"**
4. Your browser will open to GitHub OAuth page
5. **Authorize** the application
6. Return to the app - you should see **"✓ Authenticated"**

### Step 2: Configure Tailscale
1. Still in the **"Authentication"** tab
2. Paste your **Tailscale auth key** in the text field
3. Click **"Save Tailscale Key"**
4. You should see **"✓ Key configured"**

### Step 3: Repository Settings
1. Go to the **"Settings"** tab
2. Enter your **repository name** in format: `your-username/windows-11-rdp`
3. Optionally set a **custom RDP password** (leave empty for default)

## First RDP Session

### Step 1: Start RDP Session
1. Go to the **"RDP Session"** tab
2. Click **"Start RDP Session"**
3. The app will:
   - Trigger the GitHub Actions workflow
   - Monitor the setup progress
   - Display real-time status updates

### Step 2: Wait for Setup
The setup process takes about **3-5 minutes**:
1. **GitHub Actions** starts Windows environment
2. **Tailscale** installs and connects
3. **RDP** is configured and enabled
4. **Connection details** are displayed

### Step 3: Get Connection Info
Once ready, you'll see:
```
🎉 RDP Connection Ready!

Tailscale IP: 100.x.x.x
Username: runneradmin  
Password: P@ssw0rd123!
```

## Connecting from Different Devices

### Install Tailscale on Your Devices
**Before connecting**, you must install Tailscale on the device you want to connect from:

- **Windows/Mac**: [tailscale.com/download](https://tailscale.com/download)
- **Android**: Google Play Store → "Tailscale"
- **iOS**: App Store → "Tailscale" 
- **Linux**: Package manager or download from website

**Login** to Tailscale with the **same account** you used for setup!

### Windows Desktop
1. **Install Tailscale** and login
2. Open **"Remote Desktop Connection"**
3. **Computer**: Enter the Tailscale IP (e.g., `100.64.0.123`)
4. **Username**: `runneradmin`
5. **Password**: Your configured password
6. Click **"Connect"**

### Mac
1. **Install Tailscale** and login
2. Download **"Microsoft Remote Desktop"** from Mac App Store
3. Add new connection with Tailscale IP and credentials
4. Connect

### Android Phone/Tablet
1. **Install both**:
   - **"Tailscale"** from Google Play
   - **"Microsoft Remote Desktop"** from Google Play
2. **Login** to Tailscale
3. In Remote Desktop app:
   - Add new desktop
   - Use Tailscale IP and credentials
   - Connect

### iPhone/iPad
1. **Install both**:
   - **"Tailscale"** from App Store
   - **"Microsoft Remote Desktop"** from App Store
2. **Login** to Tailscale
3. Add desktop connection and connect

## Session Management

### Session Duration
- **Maximum**: 6 hours per session
- **Automatic shutdown**: After 6 hours
- **Restart**: Click "Start RDP Session" again
- **Manual stop**: Click "Stop RDP Session"

### Multiple Sessions
- You can run **multiple sessions** simultaneously
- Each gets a **unique Tailscale IP**
- Useful for different projects or testing

## Troubleshooting

### Desktop Application Issues

**"Application won't start"**
- Try running as **administrator**
- Check Windows version compatibility
- Download the correct architecture (x86/x64)
- Disable antivirus temporarily during first run

**"GitHub authentication failed"**
- Check your **internet connection**
- Try a different browser for OAuth
- Clear browser cache and cookies
- Ensure GitHub account has proper permissions

**"Tailscale key invalid"**
- Verify the key starts with `tskey-auth-`
- Check if the key has **expired**
- Generate a **new key** if needed
- Ensure key has **pre-authorization** enabled

### RDP Connection Issues

**"Can't connect to RDP"**
- **Install Tailscale** on your connecting device
- **Login** with the same Tailscale account
- Check if the GitHub workflow **completed successfully**
- Verify you're using the correct **Tailscale IP**
- Try different **RDP clients**

**"Tailscale not connecting"**
- Check **firewall settings** on both devices
- Restart Tailscale on both devices
- Verify **same account** used on both devices
- Check Tailscale **network status** in dashboard

**"Session disconnected"**
- GitHub Actions **6-hour limit** reached
- **Restart** the RDP session from the app
- Check **internet connectivity**
- Monitor GitHub Actions **usage limits**

### GitHub Actions Issues

**"Workflow failed to start"**
- Check if you've **forked** the repository
- Verify **TAILSCALE_AUTH_TOKEN** secret is set
- Ensure GitHub Actions is **enabled** in your fork
- Check GitHub Actions **usage limits**

**"Workflow runs but fails"**
- Check the **workflow logs** for error messages
- Verify Tailscale key hasn't **expired**
- Check if GitHub runner has **internet access**
- Try **restarting** the workflow

### Mobile Connection Issues

**"Can't connect from phone"**
- Install **both Tailscale AND RDP apps**
- Login to Tailscale **first**
- Use **landscape mode** for better experience
- Try **different RDP apps** if one doesn't work
- Check **mobile data/WiFi** connection

### Performance Issues

**"RDP is slow"**
- Reduce **color depth** in RDP settings
- Disable **desktop effects**
- Use **wired connection** instead of WiFi
- Close **unnecessary applications** on both ends
- Try during **off-peak hours**

## Getting Help

### Documentation and Resources
- **GitHub Issues**: [Report bugs here](https://github.com/anshuman960/windows-11-rdp/issues)
- **Tailscale Docs**: [tailscale.com/kb](https://tailscale.com/kb)
- **YouTube Tutorial**: [Reference Video](https://youtu.be/3Ash-395oCI)
- **GitHub Actions Docs**: [GitHub Actions Guide](https://docs.github.com/en/actions)

### Community Support
- Check existing **GitHub Issues** first
- Provide **detailed error messages** when reporting
- Include **system information** (OS, architecture)
- Mention **workflow run links** if applicable

### Before Reporting Issues
1. Check this **troubleshooting guide**
2. Try the **basic solutions** first
3. Check **service status** for GitHub and Tailscale
4. Test with **different devices/networks**
5. Collect **relevant log messages**

---

**Happy remote computing!** 🚀🖥️

If this guide helped you, please ⭐ **star the repository** on GitHub!