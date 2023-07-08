import tkinter as tk
import time

def update_clock():
  current_time = time.strftime("%H:%M:%S")
  clock_label.config(text = current_time)
  clock_label.after(1000, update_clock)

window = tk.Tk()
window.title("Digital Clock")

clock_label = tk.Label(window, font=("DS-Digital", 70), fg= "light grey", bg = "black")
clock_label.pack(padx=50, pady=50)

update_clock()
window.mainloop()


