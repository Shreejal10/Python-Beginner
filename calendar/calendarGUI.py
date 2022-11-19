from tkinter import *
import calendar
root = Tk()
root.title("Calendar App")
e = Entry(root)
root.config(background="black")
msg = Label(root, text="Enter a year", bg="black", fg="white", width="40")
msg.grid(row=1, column=1, pady=5)
e.grid(row=2, column=1, pady=5)
e.get()


def click():
    text = calendar.calendar(int(e.get()))
    root.geometry("550x600")
    root.title("Calendar App")
    label1 = Label(root, text="Calendar", font=(
        "Arial", 28, "bold"), bg="black", fg="white")
    label1.grid(row=1, column=1)
    root.config(background="black")

    l1 = Label(root, text=text, font=("consolas 10 bold "),justify=LEFT, bg="black", fg="white")
    l1.grid(row=2, column=1, padx=20)


button = Button(root, text="Enter", command=click)
button.grid(row=3, column=1, pady=10)
root.mainloop()
