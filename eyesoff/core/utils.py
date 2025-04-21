import os
from datetime import datetime
import cv2
import pygame

# Initialize pygame mixer once
pygame.mixer.init()

ALERT_SOUND_PATH = os.path.join("assets", "alert.mp3")
SNAPSHOT_DIR = "snapshots"
LOG_FILE = "logs.txt"

# Ensure snapshot folder exists
os.makedirs(SNAPSHOT_DIR, exist_ok=True)

def play_alert_sound():
    try:
        pygame.mixer.music.load(r"C:\Users\epoka\OneDrive\Desktop\eyesoff\assets\alert.mp3")
        pygame.mixer.music.play()
    except Exception as e:
        print(f"[⚠️] Failed to play sound: {e}")

def save_snapshot(frame, prefix="snapshot"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{timestamp}.jpg"
    path = os.path.join(SNAPSHOT_DIR, filename)
    cv2.imwrite(path, frame)
    print(f"[📸] Snapshot saved to {path}")

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[📝] [{timestamp}] {message}\n"
    print(entry.strip())

    # ✅ Write to file with emoji-safe encoding
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)
