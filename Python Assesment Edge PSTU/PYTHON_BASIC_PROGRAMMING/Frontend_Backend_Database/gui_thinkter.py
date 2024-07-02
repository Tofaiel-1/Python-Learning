from tkinter import Button, Entry, Label, Tk, mainloop

window = Tk()
# Set the initial size of the window
window.geometry("800x750")  # width x height

Label(window, text="First Name").grid(row=0)
Label(window, text="Last Name").grid(row=1)

e1 = Entry(window, width=50)
e2 = Entry(window, width=50)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(window, text="Submit").grid(row=3, column=1)

mainloop()
