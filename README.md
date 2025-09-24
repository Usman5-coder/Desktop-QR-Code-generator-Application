# 🔲 Advanced QR Code Generator

A modern, feature-rich desktop application for generating customizable QR codes with logo integration, built with Python and Tkinter.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

### 🎨 **Interactive User Interface**
- Modern, professional design with excellent typography
- Responsive layout that adapts to different screen sizes
- Intuitive control panel with organized sections
- Real-time QR code preview with instant updates

### 📷 **Logo Integration**
- Upload and embed logos directly into QR codes
- Supports multiple image formats (PNG, JPG, JPEG, GIF, BMP, TIFF)
- Automatic logo resizing and optimal positioning
- Smart background handling for better logo visibility

### 🎨 **Customizable Colors**
- Interactive color picker for foreground and background
- Visual color buttons showing current selections
- Real-time color preview and updates
- Unlimited color combinations

### 💾 **Export Functionality**
- High-resolution QR code export (superior to preview quality)
- Multiple output formats (PNG, JPEG)
- Batch export capabilities
- Quality preservation during export

### 🌙 **Theme Support**
- Light and dark theme toggle
- Consistent theming across all components
- Settings persistence between application sessions
- Eye-friendly design for extended use

### ⚙️ **Advanced Options**
- **Error Correction Levels**: Low (7%), Medium (15%), Quartile (25%), High (30%)
- **Module Styles**: Square, Rounded, Circle patterns
- **Content Types**: URLs, text, contact info, WiFi credentials, and more
- **Auto-generation**: QR codes update as you type

## 📋 Prerequisites

- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: Minimum 512MB RAM
- **Storage**: 50MB free space

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
```

### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**Or install manually:**
```bash
pip install qrcode[pil] pillow
```

### 4. Run the Application
```bash
python qr_generator.py
```

## 📖 Usage Guide

### Basic QR Code Generation
1. **Launch the application**
2. **Enter your content** in the text area (URL, text, etc.)
3. **Watch the preview** update automatically
4. **Customize appearance** using the style options
5. **Save your QR code** using the download button

### Adding a Logo
1. Click **"📁 Upload Logo"** button
2. Select an image file from your computer
3. The logo will automatically appear in the QR code center
4. Use **"❌ Remove Logo"** to remove it

### Customizing Colors
1. Click the **colored squares** next to "Foreground Color" and "Background Color"
2. Use the **color picker** to select your preferred colors
3. The QR code will **update instantly**

### Changing Themes
- Click the **theme toggle button** (🌙/☀️) in the top-right corner
- Your preference will be **saved automatically**

## 🛠️ Configuration Options

### Error Correction Levels
| Level | Recovery Capacity | Use Case |
|-------|-------------------|----------|
| **Low (7%)** | Basic protection | Clean environments |
| **Medium (15%)** | Standard protection | General use (recommended) |
| **Quartile (25%)** | High protection | Potentially damaged codes |
| **High (30%)** | Maximum protection | Harsh conditions |

### Module Styles
- **Square**: Traditional, clean appearance
- **Rounded**: Modern, soft corners
- **Circle**: Distinctive, artistic look

## 📁 File Structure

```
qr-code-generator/
├── qr_generator.py          # Main application file
├── requirements.txt         # Python dependencies
├── qr_settings.json        # User settings (auto-generated)
├── README.md               # This file
└── assets/                 # Optional assets folder
    └── screenshots/        # Application screenshots
```

## 🔧 Settings & Data

### Persistent Settings
The application automatically saves:
- **Theme preference** (light/dark)
- **Color selections** (foreground/background)
- **Window position** and size

Settings are stored in `qr_settings.json` in the application directory.

### Supported Input Types
- **URLs**: `https://example.com`
- **Plain Text**: Any text content
- **Email**: `mailto:user@example.com`
- **Phone Numbers**: `tel:+1234567890`
- **WiFi**: `WIFI:T:WPA;S:NetworkName;P:Password;;`
- **SMS**: `sms:+1234567890:Message`

## 🚨 Troubleshooting

### Common Issues

**Application won't start:**
```bash
# Check Python version
python --version

# Reinstall dependencies
pip install --upgrade qrcode[pil] pillow
```

**Logo upload fails:**
- Ensure image file is not corrupted
- Try converting to PNG format
- Check file permissions

**QR code not generating:**
- Verify input content is not empty
- Check error correction level settings
- Try restarting the application

**Theme not saving:**
- Ensure write permissions in application directory
- Check if `qr_settings.json` is not read-only

### Error Messages
| Error | Solution |
|-------|----------|
| "Invalid image file" | Use supported formats (PNG, JPG, etc.) |
| "Failed to generate QR code" | Check input content and settings |
| "Failed to save QR code" | Verify write permissions in target directory |

## 🔒 Security & Privacy

- **No Data Collection**: Application runs completely offline
- **Local Processing**: All QR generation happens on your device
- **No Network Requests**: No data sent to external servers
- **Settings Privacy**: Only UI preferences are saved locally

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes** and add tests
4. **Commit your changes**: `git commit -am 'Add feature'`
5. **Push to the branch**: `git push origin feature-name`
6. **Submit a Pull Request**

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest

# Code formatting
black qr_generator.py

# Linting
flake8 qr_generator.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

### Getting Help
- **Issues**: Report bugs on [GitHub Issues](https://github.com/yourusername/qr-code-generator/issues)
- **Discussions**: Join conversations in [GitHub Discussions](https://github.com/yourusername/qr-code-generator/discussions)
- **Email**: Contact us at support@example.com

### FAQ

**Q: Can I generate QR codes for commercial use?**
A: Yes, the generated QR codes can be used for any purpose, including commercial applications.

**Q: What's the maximum size for logos?**
A: Logos are automatically resized to 20% of the QR code dimensions for optimal scanning.

**Q: Can I batch generate multiple QR codes?**
A: Currently, the application generates one QR code at a time. Batch processing is planned for future releases.

**Q: Does the application work offline?**
A: Yes, completely offline. No internet connection required.

## 🗺️ Roadmap

### Upcoming Features
- [ ] **Batch QR Generation**: Generate multiple QR codes from CSV files
- [ ] **QR Code Scanner**: Built-in scanning functionality
- [ ] **Templates**: Pre-designed QR code templates
- [ ] **History**: Recent QR codes history
- [ ] **Export Formats**: SVG, PDF export options
- [ ] **API Integration**: Connect with popular services
- [ ] **Plugins**: Extensible plugin system

### Version History
- **v1.0.0**: Initial release with core features
- **v1.1.0**: Added theme support and logo integration
- **v1.2.0**: Enhanced UI and color customization

## 🌟 Acknowledgments

- **QRCode Library**: [python-qrcode](https://github.com/lincolnloop/python-qrcode) for QR generation
- **Pillow**: [PIL/Pillow](https://pillow.readthedocs.io/) for image processing  
- **Tkinter**: Python's built-in GUI framework
- **Icons**: Emoji icons used throughout the interface

## 📊 Statistics

- **Lines of Code**: ~500+
- **Features**: 15+ major features
- **Supported Formats**: 6+ image formats
- **Themes**: 2 (Light/Dark)
- **Platforms**: 3 (Windows/macOS/Linux)

---

<div align="center">

**Made with ❤️ by Usman**

[⭐ Star this repo](https://github.com/yourusername/qr-code-generator) | [🐛 Report Bug](https://github.com/yourusername/qr-code-generator/issues) | [💡 Request Feature](https://github.com/yourusername/qr-code-generator/issues)

</div>
