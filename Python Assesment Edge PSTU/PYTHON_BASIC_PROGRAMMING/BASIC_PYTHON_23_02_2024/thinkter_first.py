import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the window title
root.title("Hello Tkinter")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")

# Pack the label into the window
label.pack()

# Start the Tkinter event loop
root.mainloop()
