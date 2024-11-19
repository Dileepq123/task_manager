#Task Manager CLI Application

 
#Project Description
A command-line interface (CLI) application to manage tasks. Users can add, view, delete, and mark tasks as complete. Tasks are saved to and loaded from a file.

#to run the aplication
python task_manager.py
*******************************************************************
#after running aplication

Welcome to the Task Manager CLI Application!

#correct password and email to login
Enter your email: admin@task.com                   #email to login
Enter your password: admin                         #password to login

Login successful!
Tasks loaded from tasks.json.

#error if ivalid password and email
Enter your email: aa@example.com
Enter your password: password

Invalid email or password.

***********************************************************************

#task manager Menu
Task Manager Menu:
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Completed
5. Save Tasks
6. Load Tasks
7. Exit

**************************************************
#Adding the task  : Allows the user to create a new task with a title.
Enter your choice: 1
Enter task title: student address
Task 'student address' added successfully.

****************************************************
#to view the task : Displays all tasks with their ID, title, and completion status.
Enter your choice: 2

Tasks:
ID: 1, Title: student marks, Status: Not Completed
ID: 2, Title: student marks, Status: Not Completed

#if there is no task 
 No tasks available

 ***************************************************

 # to marks as completed :Marks a specific task as completed based on its ID.
Enter your choice: 4
Enter task ID to mark as completed: 2
Task with ID 2 marked as completed.

#if there is no task named 5
Enter your choice: 4
Enter task ID to mark as completed: 5
No task found with ID 5.

***************************************************
#To delete the task : Allows the user to delete a task by its unique ID.
Enter your choice: 4
Enter task ID to mark as completed: 1
Task with ID 1 marked as completed.

***************************************************
# to save task : Saves the current task list to a tasks.json file.
Enter your choice: 5
Tasks saved to tasks.json.

**************************************************
#to load the task :  Loads tasks from the tasks.json file into the application.
Enter your choice: 6
Tasks loaded from tasks.json.

**************************************************
# to exit : Exits the Task Manager application.
Enter your choice: 7
Exiting Task Manager

# if enter invalid number
Enter your choice: 9
Invalid choice. Try again.

*************************************************
overview

 login()
Purpose: Authenticates user credentials.
Input: Email, Password.
Output: Grants or denies access.

 display_menu()
Purpose: Shows the main menu options.
Input: None.
Output: Prints the menu.

add_task(tasks, title)
Purpose: Adds a new task to the list.
Input: Task list, Task title.
Output: Updates task list and confirms addition.

 view_tasks(tasks)
Purpose: Displays all tasks with details.
Input: Task list.
Output: Prints task details or "No tasks available."

delete_task(tasks, task_id)
Purpose: Removes a task by ID.
Input: Task list, Task ID.
Output: Updates task list and confirms deletion.

mark_task_completed(tasks, task_id)
Purpose: Marks a task as completed.
Input: Task list, Task ID.
Output: Updates task status and confirms action.

save_tasks(tasks, filename)
Purpose: Saves tasks to a JSON file.
Input: Task list, File name.
Output: Saves to file and confirms.

load_tasks(filename)
Purpose: Loads tasks from a JSON file.
Input: File name.
Output: Returns loaded tasks or starts fresh.


