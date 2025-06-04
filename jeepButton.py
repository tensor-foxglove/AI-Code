import tkinter as tk
from tkinter import messagebox
import threading
import os
import sys
import winsound
import simpleaudio as sa
import webbrowser

try:
    # For Windows
    def play_alarm():
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
except ImportError:
    # For other OS, use simpleaudio if available
    try:
        def play_alarm():
            wave_obj = sa.WaveObject.from_wave_file('alarm.wav')
            play_obj = wave_obj.play()
            play_obj.wait_done()
    except ImportError:
        def play_alarm():
            messagebox.showinfo("Alarm", "Alarm sound not supported on this system.")

def on_button_press():
    threading.Thread(target=play_alarm, daemon=True).start()

root = tk.Tk()
root.title("Fell For It Again!")
root.geometry("300x200")

button = tk.Button(
    root,
    text="Fell For \nIt Again!",
    font=("Arial", 24, "bold"),
    bg="blue",
    fg="white",
    width=10,
    height=3,
    command=on_button_press
)
button.pack(expand=True)

root.mainloop()