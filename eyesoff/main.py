# main.py

import os
import cv2
from gui.gui import run_gui

if __name__ == "__main__":
    # Check if webcam is available
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("[❌] No webcam detected.")
        exit()
    cam.release()

    print("[🔒] Starting EyesOff GUI...")
    run_gui()
