import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, update_time)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")
window.geometry("200x100")

# Create a label to display the time
time_label = tk.Label(window, text="", font=("Helvetica", 24))
time_label.pack(pady=30)

# Update the time initially and start the update process
update_time()

# Start the tkinter event loop
window.mainloop()
