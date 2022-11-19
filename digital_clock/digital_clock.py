from tkinter import Tk
from tkinter import Label
import time
root = Tk()
root.title("Digital Clock")

# function to update the time


def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)


clock = Label(root, font=("Arial", 90), bg="black", fg="white")
clock.pack()
get_time()


root.mainloop()
