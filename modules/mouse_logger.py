# To capture mouse movement

from pynput import mouse
from .logger_utils import write_log

def on_click(x, y, button, pressed):
    if pressed:
        write_log(f"[MOUSE CLICK] {button} at ({x}, {y})")

def on_scroll(x, y, dx, dy):
    write_log(f"[MOUSE SCROLL] at ({x}, {y}) | dx={dx}, dy={dy}")

def start_mouse_logger():
    listener = mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll
    )
    listener.start()
    listener.join()
