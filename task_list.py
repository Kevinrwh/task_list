# This project is a CLI-based task list that allows a user to add, view, and complete tasks

# Our list to store tasks
tasks = []

# USER INTERFACE
# Show the menu to the user 
def show_menu():
    print("Task List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

# TASK MANAGEMENT METHODS

# Add: Add a task to the list
def add_task(title, description):

    # Task is a dictionary object (k-v pairs)
    task = {"title": title, "description": description, "completed": False} 
    tasks.append(task)
    print("Task added.")

# View: View all current tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
        
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{i}. {task['title']} - {status}") # f-string (formatted string)

# Mark complete: Mark a task as complete 
def mark_task_completed(task_index):
    if 0 <= task_index < len(tasks): # if in list
        tasks[task_index]["completed"] = True # mark complete
        print("Task completed.")
    else:
        print("Invalid task index.") # not in list

# Remove: Remove a task from the list 
def remove_task(task_index):
    if 0 <= task_index < len(tasks): #if in list
        del tasks[task_index] # delete dict member from the list
        print("Task deleted.")
    else:
        print("Invalid task index.") # not in list

# Get user input
def get_user_input():
    choice = input("Enter your choice: ")
    return choice

# MAIN
def main():
    while True:
        # Show menu and get input
        show_menu()
        choice = get_user_input()

        # Based on input, do the action
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task number to mark as completed: "))
        elif choice == "4":
            task_index = int(input("Enter the task number to delete: "))
            remove_task(task_index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select a valid choice: ")
    
if __name__ == "__main__":
    main()
