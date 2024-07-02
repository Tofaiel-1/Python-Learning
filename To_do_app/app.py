import os

class Task:
    def __init__(self, title, description, priority, deadline, completed=False):
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.completed = completed

class TodoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, priority, deadline):
        priority = priority.lower()
        if priority in ['high', 'medium', 'low']:
            task = Task(title, description, priority, deadline)
            self.tasks.append(task)
            print(f"Task '{title}' added to the to-do list.")
        else:
            print("Invalid priority. Please enter 'High', 'Medium', or 'Low'.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return
        print("To-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. Title: {task.title}, Priority: {task.priority}, Deadline: {task.deadline}, Completed: {task.completed}")

    def mark_task_as_done(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print(f"Task '{self.tasks[task_index - 1].title}' marked as done.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task.title}' deleted.")
        else:
            print("Invalid task index.")

    def edit_task(self, task_index, title=None, description=None, priority=None, deadline=None):
        if 0 < task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            if title:
                task.title = title
            if description:
                task.description = description
            if priority:
                priority = priority.lower()
                if priority in ['high', 'medium', 'low']:
                    task.priority = priority
                else:
                    print("Invalid priority. Please enter 'High', 'Medium', or 'Low'.")
            if deadline:
                task.deadline = deadline
            print(f"Task '{task.title}' updated.")
        else:
            print("Invalid task index.")

    def save_tasks_to_file(self, filename):
        file_path = os.path.join(os.path.dirname(__file__), filename)
        with open(file_path, 'w') as file:
            for task in self.tasks:
                file.write(f"Title: {task.title}\n")
                file.write(f"Description: {task.description}\n")
                file.write(f"Priority: {task.priority}\n")
                file.write(f"Deadline: {task.deadline}\n")
                file.write(f"Completed: {task.completed}\n")
                file.write("\n")
        print("Tasks saved to file successfully.")

    def load_tasks_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks_data = []
                lines = file.readlines()
                task_data = {}
                for line in lines:
                    if line.strip():
                        key, value = line.split(': ')
                        task_data[key.strip()] = value.strip()
                    else:
                        tasks_data.append(task_data)
                        task_data = {}
                for task_data in tasks_data:
                    self.tasks.append(Task(
                        task_data['Title'],
                        task_data['Description'],
                        task_data['Priority'],
                        task_data['Deadline'],
                        task_data['Completed'] == 'True'
                    ))
            print("Tasks loaded from file successfully.")
        except FileNotFoundError:
            print("File not found.")

# Main function
def main():
    manager = TodoListManager()

    while True:
        print("\n-- To-Do List Manager Menu --")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Filter Tasks")
        print("7. Sort Tasks")
        print("8. Search Tasks")
        print("9. Save Tasks to File")
        print("10. Load Tasks from File")
        print("11. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            deadline = input("Enter task deadline (YYYY-MM-DD): ")
            manager.add_task(title, description, priority, deadline)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to mark as done: "))
            manager.mark_task_as_done(task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to delete: "))
            manager.delete_task(task_index)
        elif choice == "5":
            task_index = int(input("Enter task index to edit: "))
            title = input("Enter new task title (press Enter to skip): ")
            description = input("Enter new task description (press Enter to skip): ")
            priority = input("Enter new task priority (press Enter to skip): ")
            deadline = input("Enter new task deadline (YYYY-MM-DD) (press Enter to skip): ")
            manager.edit_task(task_index, title, description, priority, deadline)
        elif choice == "9":
            filename = input("Enter filename to save tasks: ")
            manager.save_tasks_to_file(filename)
        elif choice == "10":
            filename = input("Enter filename to load tasks from: ")
            file = open("example.txt", "r")

            print("Invalid choice. Please enter a number between 1 and 11.")

if __name__ == "__main__":
    main()
