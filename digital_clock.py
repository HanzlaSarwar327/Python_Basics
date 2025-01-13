import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')  # Get current time in HH:MM:SS AM/PM format
    label.config(text=string)
    label.after(1000, time)  # Update the time every second

# Create the window
root = tk.Tk()
root.title("Digital Clock")

# Create the label to display the time
label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

time()  # Call the time function to start updating the clock
root.mainloop()
