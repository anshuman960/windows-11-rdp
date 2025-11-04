# Windows 11 RDP via GitHub Actions 🖥️ (Now with Tailscale)

A GitHub Actions workflow that creates a **free, secure Windows 11 Remote Desktop Protocol (RDP)** environment using **Tailscale VPN**. Perfect for development, testing, and accessing Windows applications remotely from any device including mobile phones.

## 🔄 Major Update (November 2025)

### ⚠️ **Ngrok Completely Removed**
We have **completely eliminated** all ngrok-based tunneling and dependencies from this repository.

### ✨ **Why We Switched to Tailscale**

**Security Advantages:**
- 🔒 **Enterprise-grade encryption**: Uses WireGuard protocol for end-to-end encryption
- 🏠 **Private mesh network**: No public URLs exposed to the internet
- 🛡️ **Zero-trust architecture**: Only authorized devices can connect
- 🎯 **Granular access control**: Role-based permissions and ACLs

**Cost & Accessibility:**
- 🆓 **No credit card required**: Tailscale's free tier covers personal use completely
- 💳 **Ngrok limitations**: Requires credit card for sustained access and advanced security features
- ♾️ **Unlimited personal use**: No arbitrary connection limits or timeouts

**Ease of Use:**
- 📦 **Simple device management**: All connected devices visible in Tailscale dashboard
- 🔌 **Automatic reconnection**: Built-in resilience and connection recovery
- 📱 **Cross-platform**: Works seamlessly on Windows, Mac, Linux, iOS, Android

*Reference: Inspired by [this YouTube tutorial](https://youtu.be/3Ash-395oCI)*

## ✨ Features

- **Free Windows Server 2022** (GitHub Actions Runner)
- **7 GB RAM** and **2 CPU cores**
- **14 GB SSD storage**
- **High-speed internet** connection
- **Pre-installed software** (VS Code, Git, Node.js, Python, etc.)
- **Secure Tailscale VPN** for private access
- **Up to 6 hours** session duration
- **Custom password** support
- **Cross-platform compatibility** (Windows, Mac, Linux, Android, iOS)
- **Easy setup** with GitHub OAuth integration

## 🚀 Quick Setup

### 1. Fork this Repository
Click the **Fork** button at the top right of this page to create your own copy.

### 2. Create Tailscale Account
1. Go to [tailscale.com](https://tailscale.com/)
2. Click **"Start connecting devices"**
3. **Sign up with GitHub** (recommended for easy OAuth)
4. **No credit card required** for personal use

### 3. Generate Tailscale Auth Key
1. In your Tailscale dashboard, go to **Settings** → **Keys**
2. Click **"Generate auth key"**
3. Leave default settings and click **"Generate key"**
4. **Copy the generated key** (starts with `tskey-auth-...`)

### 4. Add GitHub Secret
1. Go to your forked repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `TAILSCALE_AUTH_TOKEN`
5. Value: Paste your Tailscale auth key
6. Click **Add secret**

### 5. Run the Workflow
1. Go to the **Actions** tab in your repository
2. Click on **"Windows 11 RDP with Tailscale"** workflow
3. Click **Run workflow**
4. Optionally set a custom password (default: `P@ssw0rd123!`)
5. Click **Run workflow**

### 6. Install Tailscale on Your Device
1. Download Tailscale for your platform:
   - **Windows/Mac**: [tailscale.com/download](https://tailscale.com/download)
   - **Android**: Google Play Store
   - **iOS**: App Store
   - **Linux**: Package manager or download
2. **Login with the same account** you used for setup
3. Wait for the GitHub runner to appear in your Tailscale network

### 7. Connect via RDP
1. Check the workflow logs for connection details
2. Use any RDP client to connect:
   - **Windows**: Remote Desktop Connection
   - **Mac**: Microsoft Remote Desktop
   - **Linux**: Remmina or xfreerdp
   - **Android/iOS**: Microsoft Remote Desktop app
3. Connect to the **Tailscale IP** shown in the logs
4. Use the provided credentials

## 📋 Connection Details

**Default Credentials:**
- **Username**: `runneradmin`
- **Password**: `P@ssw0rd123!` (or your custom password)
- **IP Address**: Provided in workflow logs (e.g., `100.x.x.x`)

**System Specifications:**
- **OS**: Windows Server 2022 (latest)
- **RAM**: 7 GB
- **CPU**: 2 cores
- **Storage**: 14 GB SSD
- **Network**: High-speed internet via Tailscale VPN
- **GPU**: Software rendering only (no dedicated GPU)

## 📱 Mobile Device Setup

### Android Devices
1. Install **Microsoft Remote Desktop** from Google Play Store
2. Install **Tailscale** from Google Play Store
3. Login to Tailscale with your account
4. In Remote Desktop app, add new connection
5. Use the Tailscale IP from workflow logs
6. Credentials: `runneradmin` / your password

### iOS Devices (iPhone/iPad)
1. Install both **Microsoft Remote Desktop** and **Tailscale** from App Store
2. Login to Tailscale
3. Add desktop connection in RDP app
4. Use Tailscale IP and credentials

## 🛠️ Pre-installed Software

Your RDP environment comes with:
- Google Chrome & Microsoft Edge
- Visual Studio Code
- Git
- Node.js & npm
- Python 3.x
- PowerShell 7
- Windows Terminal
- .NET Framework
- And many more development tools!

## 🚀 Coming Soon: Desktop Application

We're developing a **PyQt5 desktop application** that will:
- ⚙️ **One-click setup**: Automate the entire process
- 🔑 **Key management**: Store and manage Tailscale auth keys securely
- 📊 **Live monitoring**: Real-time status of your RDP sessions
- 📁 **GitHub integration**: OAuth login and workflow management
- 💻 **Cross-architecture**: Support both x86 (32-bit) and x64 (64-bit) Windows
- 📦 **Easy distribution**: Downloadable .exe files from GitHub Releases

## 🔧 Troubleshooting

### Common Issues

**"Tailscale authentication failed"**
- Ensure your `TAILSCALE_AUTH_TOKEN` secret is set correctly
- Verify the token hasn't expired
- Check your Tailscale account status

**"Cannot connect to RDP"**
- Ensure Tailscale is installed and logged in on your device
- Verify you're using the correct Tailscale IP from the logs
- Check that both devices are in the same Tailscale network
- Try different RDP clients

**"Workflow fails to start"**
- Check if you have GitHub Actions enabled
- Verify the workflow file exists in `.github/workflows/`
- Ensure you have the required repository permissions

## 📝 Important Notes

### Limitations
- **6-hour maximum**: Sessions automatically terminate after 6 hours
- **No persistent storage**: Files are lost when session ends
- **No dedicated GPU**: GitHub Actions runners don't have graphics cards
- **Network dependency**: Requires Tailscale connection on both ends

### Security Best Practices
- Use strong, custom passwords
- Don't store sensitive data on the RDP session
- Monitor your Tailscale network for unauthorized devices
- Use Tailscale ACLs for additional access control
- Keep your auth keys secure and rotate them regularly

### Usage Guidelines
- Use for development and testing only
- Respect GitHub's Terms of Service and fair usage policies
- Don't use for mining, illegal activities, or production workloads
- Monitor resource usage to avoid account restrictions

## 🎆 Advantages Over Previous Ngrok Version

| Feature | Tailscale (Current) | Ngrok (Removed) |
|---------|-------------------|------------------|
| **Security** | Private mesh VPN, WireGuard encryption | Public tunnel, basic auth |
| **Cost** | Free for personal use | Credit card required for features |
| **Setup** | OAuth + auth key | Manual token management |
| **Mobile** | Native apps available | Web-based only |
| **Reliability** | Auto-reconnection | Manual tunnel management |
| **Privacy** | Zero public exposure | Public endpoint required |

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs or security issues
- Suggest improvements for mobile compatibility
- Submit pull requests for new features
- Share your use cases and feedback
- Help with the upcoming desktop application

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This project is for educational and development purposes only. Users are responsible for complying with:
- GitHub Terms of Service
- Tailscale Terms of Service  
- Local laws and regulations

The author is not responsible for any misuse of this tool.

## 🌟 Show Your Support

If this project helped you, please give it a ⭐ star on GitHub!

---

**Secure remote access with Tailscale!** 🚀🔒