# Collects IP, hostname, OS details

import socket
import platform
import requests
from .logger_utils import write_log

def capture_system_info():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        public_ip = requests.get("https://api.ipify.org").text
        os_info = platform.platform()
        user = platform.node()

        write_log("[SYSTEM INFO]")
        write_log(f"Hostname: {hostname}")
        write_log(f"Username: {user}")
        write_log(f"Local IP: {local_ip}")
        write_log(f"Public IP: {public_ip}")
        write_log(f"OS: {os_info}")
        write_log("-" * 40)

    except Exception as e:
        write_log(f"[ERROR] Could not gather system info: {e}")
