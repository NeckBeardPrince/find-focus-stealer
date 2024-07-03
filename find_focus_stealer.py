#!/usr/bin/python

from AppKit import NSWorkspace
import os
import time
from datetime import datetime

# Define the ANSI escape code for red text and reset
GREEN_TEXT = "\033[92m"
RED_TEXT = "\033[5m\033[91m"  # Blinking + Red
RESET_TEXT = "\033[0m"

workspace = NSWorkspace.sharedWorkspace()
active_app = workspace.activeApplication()["NSApplicationName"]
t = datetime.now().strftime("%H:%M:%S.%f")
if active_app == "CoreServicesUIAgent":
    os.system("say 'Focus Stealer Alert'")
    print("Active focus: " + RED_TEXT + active_app + " @ " + t)
else:
    print("Active focus: " + GREEN_TEXT + active_app + RESET_TEXT + " @ " + t)
while True:
    time.sleep(1)
    t = datetime.now().strftime("%H:%M:%S.%f")
    prev_app = active_app
    active_app = workspace.activeApplication()["NSApplicationName"]
    if prev_app != active_app:
        if active_app == "CoreServicesUIAgent":
            os.system("say 'Focus Stealer Alert'")
            print("Focus changed to: " + RED_TEXT + active_app + RESET_TEXT + " @ " + t)
        else:
            print(
                "Focus changed to: " + GREEN_TEXT + active_app + RESET_TEXT + " @ " + t
            )
