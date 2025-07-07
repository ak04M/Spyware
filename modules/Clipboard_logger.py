# For collecting 'paste' content by the clipboard

import time
import pyperclip
from .logger_utils import write_log

def start_clipboard_logger():
    recent_value = ""
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            write_log(f"[CLIPBOARD] {recent_value}")
        time.sleep(2)
