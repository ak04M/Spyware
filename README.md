# macOS Spyware (Red Team Educational Tool)

This project is a modular spyware framework for macOS, designed for ethical hacking practice and red team development. It demonstrates how various components of a surveillance tool can be combined into a persistent and stealthy payload.

> ❗️This tool is for educational and authorized security research purposes only.

## 🔧 Features

- 🔑 Keylogger (using `pynput`)
- 📋 Clipboard logger
- 🖱️ Mouse activity tracker
- 📸 Screenshot capture loop
- 🪟 Active window title tracker
- 🛜 Discord webhook exfiltration
- 🧠 System info grabber
- ♻️ Persistence via LaunchAgents (`.plist`)
- 🎯 Modular design (easy to extend)

## 💻 Platform Support

- ✅ macOS (tested on Python 3.13+)
- ❌ Not compatible with Windows/Linux (yet)

## 📁 Project Structure

<PRE><CODE>
spyware-mac/
├── spyware.py                # Main launcher script (calls all modules)
├── create_persistence.py     # Auto-generates LaunchAgent plist
├── requirements.txt          # List of dependencies
├── README.md                 # Full project explanation
├── LICENSE                   # "Ethical red team use only" license
├── .gitignore                # Prevents logs/screenshots from being committed
├── modules/                  # Core functionality modules
│   ├── keylogger.py
│   ├── mouse_logger.py
│   ├── clipboard_logger.py
│   ├── screenshotter.py
│   ├── window_tracker.py
│   ├── system_info.py
│   ├── exfil.py
│   └── logger_utils.py
└── logs/                     # Local output storage (ignored in Git)
    ├── activity.log
    ├── screenshot_*.png
    └── system.txt
</CODE></PRE>


## 🚨 Disclaimer

This repository is intended **solely for ethical red team simulation**, training, and research in controlled environments. **Unauthorized deployment of this tool is strictly prohibited.**

By using this code, you agree to use it responsibly and within all legal and ethical boundaries.
The author is not responsible for any kind of misuse of this code.

## Author

Ankush Kumar Mohapatra
IIIT BBSR
