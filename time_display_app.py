import datetime
import time
import tkinter as tk
from tkinter import ttk

def get_current_time():
    """Gets the current time in HH:MM:SS format."""
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def get_utc_time():
    """Gets the current time in UTC in HH:MM:SS format."""
    now = datetime.datetime.utcnow()
    return now.strftime("%H:%M:%S")

def update_time_labels():
    """Updates the time labels with the current system time and UTC time."""
    system_time_label.config(text="System Time\n" + get_current_time())
    utc_time_label.config(text="UTC Time\n" + get_utc_time())
    root.after(1000, update_time_labels)  # Schedule the update after 1000 milliseconds (1 second)

root = tk.Tk()
root.title("Time Display")

window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

arial = ("Arial", 30)

style = ttk.Style()
style.configure("TLabel", font=arial, anchor="center", justify="center")

system_time_label = ttk.Label(root, style="TLabel")
system_time_label.pack(fill=tk.BOTH, expand=True)

utc_time_label = ttk.Label(root, style="TLabel")
utc_time_label.pack(fill=tk.BOTH, expand=True)

update_time_labels()

root.mainloop()
