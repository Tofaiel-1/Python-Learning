# Define global variables
todos = []

# Function to add a task to the to-do list
def add_task(task):
    todos.append(task)
    print("Task added successfully!")

# Function to remove a task from the to-do list
def remove_task(task):
    if task in todos:
        todos.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found in the list.")

# Function to display the to-do list
def display_tasks():
    if todos:
        print("Your To-Do List:")
        for index, task in enumerate(todos, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

# Main program loop
while True:
    print("\nWelcome to To-Do List Manager!")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("Thank you for using To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
  