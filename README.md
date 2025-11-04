# Windows 11 RDP via GitHub Actions 🖥️

A GitHub Actions workflow that creates a **free Windows 11 Remote Desktop Protocol (RDP)** environment using ngrok tunneling. Perfect for development, testing, and accessing Windows applications remotely from any device including mobile phones.

## ✨ Features

- **Free Windows Server 2022** (GitHub Actions Runner)
- **7 GB RAM** and **2 CPU cores**
- **14 GB SSD storage**
- **High-speed internet** connection
- **Pre-installed software** (VS Code, Git, Node.js, Python, etc.)
- **Secure ngrok tunnel** for RDP access
- **Up to 6 hours** session duration
- **Custom password** support
- **Cross-platform compatibility** (Windows, Mac, Linux, Android, iOS)
- **Easy one-click setup**

## 🚀 Quick Setup

### 1. Fork this Repository
Click the **Fork** button at the top right of this page to create your own copy.

### 2. Get Ngrok Auth Token
1. Sign up for a free account at [ngrok.com](https://ngrok.com/)
2. Go to your [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken)
3. Copy your authentication token

### 3. Add GitHub Secret
1. Go to your forked repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `NGROK_AUTH_TOKEN`
5. Value: Paste your ngrok auth token
6. Click **Add secret**

### 4. Run the Workflow
1. Go to the **Actions** tab in your repository
2. Click on **Windows 11 RDP** workflow
3. Click **Run workflow**
4. Optionally set a custom password (default: `P@ssw0rd123!`)
5. Click **Run workflow**

### 5. Connect to RDP
1. Wait for the workflow to complete (about 2-3 minutes)
2. Check the workflow logs for connection details
3. Use any RDP client to connect:
   - **Windows**: Remote Desktop Connection
   - **Mac**: Microsoft Remote Desktop
   - **Linux**: Remmina or xfreerdp
   - **Android**: Microsoft Remote Desktop, RD Client
   - **iOS**: Microsoft Remote Desktop, RD Client
   - **Web**: HTML5 RDP clients

## 📋 Connection Details

**Default Credentials:**
- **Username**: `runneradmin`
- **Password**: `P@ssw0rd123!` (or your custom password)

**System Specifications:**
- **OS**: Windows Server 2022 (latest)
- **RAM**: 7 GB
- **CPU**: 2 cores
- **Storage**: 14 GB SSD
- **Network**: High-speed internet
- **GPU**: Note: GitHub Actions runners do not have dedicated GPUs

## 📱 Mobile Device Setup

### Android Devices
1. Install **Microsoft Remote Desktop** from Google Play Store
2. Open the app and tap **+** to add a new connection
3. Enter the ngrok tunnel URL (without tcp:// prefix)
4. Username: `runneradmin`
5. Password: Your set password
6. Tap **Save** and then connect

### iOS Devices (iPhone/iPad)
1. Install **Microsoft Remote Desktop** from App Store
2. Tap **+** and select **Desktop**
3. Enter the ngrok tunnel URL in **PC name**
4. Add credentials: Username `runneradmin` and your password
5. Tap **Save** and connect

### Mobile Optimization Tips
- Use landscape mode for better experience
- Enable "Fit screen" or "Zoom" mode in RDP app settings
- Consider using a Bluetooth keyboard and mouse for extended use
- Adjust display scaling in Windows for mobile-friendly interface

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

## ⚙️ Advanced Configuration

### Custom Password
You can set a custom RDP password when running the workflow:
1. Click **Run workflow**
2. Enter your desired password in the "Custom RDP Password" field
3. Click **Run workflow**

### Extending Session Time
By default, sessions run for up to 6 hours. You can:
- Cancel and restart the workflow to reset the timer
- Modify the timeout in `.github/workflows/rdp.yml` (line 28)

### Multiple Sessions
You can run multiple workflows simultaneously, each will get a unique ngrok URL.

### Mobile-Friendly Settings
The workflow automatically configures Windows for better mobile compatibility:
- Optimized display scaling
- Touch-friendly interface elements
- Improved on-screen keyboard support

## 🔧 Troubleshooting

### Common Issues

**"Ngrok authentication failed"**
- Ensure your `NGROK_AUTH_TOKEN` secret is set correctly
- Verify the token is valid on your ngrok dashboard

**"Cannot connect to RDP"**
- Check the workflow logs for the correct tunnel URL
- Ensure you're using the full address without "tcp://" prefix
- Try different RDP clients

**"Workflow fails to start"**
- Check if you have GitHub Actions enabled in your repository
- Ensure the workflow file is in `.github/workflows/` directory

**Mobile Connection Issues**
- Ensure your mobile device has stable internet connection
- Try using different RDP apps if one doesn't work
- Check if the ngrok tunnel is still active
- Verify credentials are entered correctly

### Getting Help
- Check the [Issues](https://github.com/anshuman960/windows-11-rdp/issues) page
- Review workflow logs for detailed error messages
- Ensure your ngrok account has available tunnel slots

## 📝 Important Notes

### Limitations
- **No dedicated GPU**: GitHub Actions runners don't have dedicated graphics cards
- **6-hour maximum**: Sessions automatically terminate after 6 hours
- **Public IP**: Your RDP session will have a public ngrok URL
- **No persistent storage**: Files are lost when the session ends
- **Mobile performance**: May be slower on mobile devices compared to desktop

### Security Considerations
- Use strong passwords
- Don't store sensitive data on the RDP session
- Be aware that this creates a publicly accessible RDP endpoint
- Monitor your ngrok usage to avoid hitting limits
- Be cautious when using on public WiFi networks

### Best Practices
- Use for development and testing only
- Don't use for mining, illegal activities, or production workloads
- Respect GitHub's Terms of Service and fair usage policies
- Keep your ngrok auth token secure
- Consider using VPN when connecting from mobile devices on public networks

## 📱 Recommended Mobile RDP Apps

| Platform | App Name | Features |
|----------|----------|----------|
| Android | Microsoft Remote Desktop | Official, free, full-featured |
| Android | RD Client | Alternative with good performance |
| Android | Chrome Remote Desktop | Web-based alternative |
| iOS | Microsoft Remote Desktop | Official, optimized for iPad/iPhone |
| iOS | Jump Desktop | Premium option with advanced features |

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements for mobile compatibility
- Submit pull requests
- Share your mobile use cases

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This project is for educational and development purposes only. Users are responsible for complying with:
- GitHub Terms of Service
- Ngrok Terms of Service
- Local laws and regulations

The author is not responsible for any misuse of this tool.

## 🌟 Show Your Support

If this project helped you, please give it a ⭐ star on GitHub!

---

**Happy Coding from anywhere!** 🚀📱