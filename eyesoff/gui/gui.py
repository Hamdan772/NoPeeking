# gui/gui.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from tkinter import messagebox
from core.eyesoff_core import run_eyesoff
import threading

def run_gui():
    def on_start():
        messagebox.showinfo("EyesOff", "Monitoring started.\nPress 'Q' in the webcam window to stop.")
        threading.Thread(target=run_eyesoff, daemon=True).start()

    def on_quit():
        root.destroy()

    root = tk.Tk()
    root.title("EyesOff")
    root.geometry("300x160")
    root.resizable(False, False)

    title = tk.Label(root, text="EyesOff", font=("Helvetica", 18, "bold"))
    title.pack(pady=15)

    start_btn = tk.Button(root, text="Start Monitoring", width=25, command=on_start)
    start_btn.pack(pady=5)

    quit_btn = tk.Button(root, text="Quit", width=25, command=on_quit)
    quit_btn.pack(pady=5)

    credits = tk.Label(root, text="👁 Privacy by EyesOff", font=("Helvetica", 8))
    credits.pack(pady=10)

    root.mainloop()

# Allow running this file directly
if __name__ == "__main__":
    run_gui()
