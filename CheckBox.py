import tkinter as tk
import json

# Function to create a checkbox
def create_checkbox(frame, text):
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(frame, text=text, variable=var)
    checkbox.pack(side=tk.LEFT)
    return var

# Function to save the checkbox states to a JSON file
def save_checkbox_states(checkbox_states):
    with open("checkbox_states.json", "w") as file:
        json.dump(checkbox_states, file)

# Function to load the checkbox states from a JSON file
def load_checkbox_states():
    try:
        with open("checkbox_states.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Create the root window
root = tk.Tk()
root.title("Daily Checkboxes")

# Create months list
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Initialize dictionary to store checkbox states
checkbox_states = load_checkbox_states()

# Create checkboxes for each month
for month in months:
    month_frame = tk.Frame(root)
    month_label = tk.Label(month_frame, text=month)
    month_label.pack()
    month_frame.pack()

    # Create checkboxes for each day
    for day in range(1, 32):
        day_frame = tk.Frame(month_frame)
        day_label = tk.Label(day_frame, text=str(day))
        day_label.pack(side=tk.LEFT)

        # Create checkboxes for each time
        time_vars = []
        for time in range(1, 6):
            checkbox_var = create_checkbox(day_frame, f"Time {time}")
            time_vars.append(checkbox_var)

        # Retrieve and set the saved state of the checkboxes
        key = f"{month}_{day}"
        if key in checkbox_states:
            saved_states = checkbox_states[key]
            for checkbox_var, state in zip(time_vars, saved_states):
                checkbox_var.set(state)

        day_frame.pack()

# Function to save checkbox states before closing
def on_closing():
    checkbox_states.clear()
    for month in months:
        for day in range(1, 32):
            key = f"{month}_{day}"
            checkbox_states[key] = [var.get() for var in time_vars]
    save_checkbox_states(checkbox_states)
    root.destroy()

# Bind the closing event to the on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the application
root.mainloop()
