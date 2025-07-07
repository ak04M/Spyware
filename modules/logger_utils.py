# Collects and stores datas in logs

import os

LOG_PATH = os.path.join("logs", "activity.log")

def write_log(data):
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(data + "\n")
