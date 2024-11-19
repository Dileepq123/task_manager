import json

# Global Variables
tasks = []
DUMMY_CREDENTIALS = {"task@basic.com": "password123"}  # Dummy credentials for testing

# Task Class
class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

    @staticmethod
    def from_dict(data):
        return Task(data["id"], data["title"], data["completed"])

# Task Management Functions
def add_task(title):
    
    #Add a new task to the task list.
    
    task_id = len(tasks) + 1
    new_task = Task(task_id, title)
    tasks.append(new_task)
    print(f"Task '{title}' added successfully.")

def view_tasks():
    
    #Display all tasks with their completion status.
    
    if not tasks:
        print("No tasks available.")
        return

    print("\nTasks:")
    for task in tasks:
        status = "Completed" if task.completed else "Not Completed"
        print(f"ID: {task.id}, Title: {task.title}, Status: {status}")

def delete_task(task_id):
    
    # Delete a task by its ID.
    
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    print(f"Task with ID {task_id} deleted.")

def mark_task_completed(task_id):
    
    #Mark a task as completed by its ID.
    
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            print(f"Task with ID {task_id} marked as completed.")
            return
    print(f"No task found with ID {task_id}.")

# File Handling Functions
def save_tasks():
    
    #Save tasks to a JSON file.
    
    with open("tasks.json", "w") as file:
        json.dump([task.to_dict() for task in tasks], file)
    print("Tasks saved to tasks.json.")

def load_tasks():
    
    #Load tasks from a JSON file.
    
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = [Task.from_dict(data) for data in json.load(file)]
        print("Tasks loaded from tasks.json.")
    except FileNotFoundError:
        tasks = []
        print("No tasks file found. Starting fresh.")

# Login System
def login():
    
    #Dummy login system using predefined credentials.
    
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if DUMMY_CREDENTIALS.get(email) == password:
        print("Login successful!")
        return True
    else:
        print("Invalid email or password.")
        return False

# Display Menu
def display_menu():
    
    #Display the task manager menu.
    
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")

# Main Function
def main():
    
    #Main function to run the Task Manager application.
    
    print("Welcome to the Task Manager CLI Application!")

    # Login process
    if not login():
        print("Exiting application due to failed login.")
        return

    # Load existing tasks if available
    load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_completed(task_id)
        elif choice == "5":
            save_tasks()
        elif choice == "6":
            load_tasks()
        elif choice == "7":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Entry Point
if __name__ == "__main__":
    main()
