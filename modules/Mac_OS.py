# Collects macOS-specific behavior (platform independent)

import time
from AppKit import NSWorkspace
from .logger_utils import write_log

def get_active_window_title():
    return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']

def start_window_logger():
    last_window = ""
    while True:
        current_window = get_active_window_title()
        if current_window != last_window:
            write_log(f"[WINDOW] {current_window}")
            last_window = current_window
        time.sleep(2)
