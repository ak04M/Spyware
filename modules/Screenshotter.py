# To capture and collect screenshots every minute

import pyautogui
import time
import os

def start_screenshot_loop():
    count = 0
    while True:
        filename = f"logs/screenshot_{count}.png"
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        count += 1
        time.sleep(60)  # One screenshot per minute
