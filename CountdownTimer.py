import tkinter as tk
from datetime import datetime, timedelta

# Enter your future time here in the format (you don't have to set all of them, just the previous up to) year, month, day, hour, minute, second, microsecond
timesetter = datetime()

# Size of the tkinter label
HEIGHT = 250
WIDTH = 1000

class CountdownTimer:
    # Creates timer and displays the time
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer")

        self.time_remaining = tk.StringVar()
        self.time_remaining.set("00:00:00")
        self.time_label = tk.Label(master, textvariable=self.time_remaining, font=("Helvetica", 48))
        self.time_label.pack()

        self.update_time_remaining()

    # Updates the time every 1000 ms
    def update_time_remaining(self):
        time_left = timesetter - datetime.now()
        time_left_str = str(time_left).split(".")
        self.time_remaining.set(time_left_str)
        self.master.after(1000, self.update_time_remaining)

# Calling functions and looping
root = tk.Tk()
timer = CountdownTimer(root)
root.mainloop()
