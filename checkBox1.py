import tkinter as tk

# Function to create a checkbox
def create_checkbox(frame, text):
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(frame, text=text, variable=var)
    checkbox.pack(side=tk.LEFT)
    return var

# Function to update checkboxes based on the selected month
def update_checkboxes():
    selected_month = month_var.get()
    for month, frame in zip(months, month_frames):
        if month == selected_month:
            frame.pack()
        else:
            frame.pack_forget()

# Create the root window
root = tk.Tk()
root.title("Daily Checkboxes")

# Create months list
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Create a variable to store the selected month
month_var = tk.StringVar(root)
month_var.set(months[0])  # Set the default selected month

# Create a spinbox to select the month
month_spinbox = tk.Spinbox(root, values=months, textvariable=month_var, command=update_checkboxes)
month_spinbox.pack()

# Create a list to store checkbox variables and frames
checkbox_vars = []
month_frames = []

# Create checkboxes for each month
for month in months:
    month_frame = tk.Frame(root)
    month_label = tk.Label(month_frame, text=month)
    month_label.pack()
    month_frames.append(month_frame)

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
            checkbox_vars.append(checkbox_var)

        day_frame.pack()

# Function to save checkbox states to a text file
def save_checkbox_states():
    with open("checkbox_states.txt", "w") as file:
        for var in checkbox_vars:
            state = "1" if var.get() else "0"
            file.write(state)
        file.write("\n")

# Create a button to save the checkbox states
save_button = tk.Button(root, text="Save", command=save_checkbox_states)
save_button.pack()

# Update checkboxes initially
update_checkboxes()

# Run the application
root.mainloop()
