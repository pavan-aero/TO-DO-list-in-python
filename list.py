# Define an empty list to store tasks
tasks = []

# Define a function to add tasks to the list
def add_task():
    task = input("Enter the task description: ")
    tasks.append(task)
    print("Task added successfully!")

# Define a function to display the list of tasks
def display_tasks():
    if len(tasks) == 0:
        print("No tasks found!")
    else:
        print("Task List:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

# Define a function to mark tasks as completed
def complete_task():
    task_index = int(input("Enter the task number to mark as completed: "))
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task number!")
    else:
        tasks.pop(task_index-1)
        print("Task marked as completed!")

# Define a function to update task descriptions
def update_task():
    task_index = int(input("Enter the task number to update: "))
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task number!")
    else:
        new_task = input("Enter the new task description: ")
        tasks[task_index-1] = new_task
        print("Task updated successfully!")

# Define a function to remove tasks from the list
def remove_task():
    task_index = int(input("Enter the task number to remove: "))
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task number!")
    else:
        tasks.pop(task_index-1)
        print("Task removed successfully!")

# Define a function to display the menu of options
def display_menu():
    print("To-Do List Application")
    print("---------------------")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Remove Task")
    print("6. Exit")

# Define the main function to run the application
def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice:"))
        if choice == 1:
            add_task()
        elif choice == 2:
            display_tasks()
        elif choice == 3:
            complete_task()
        elif choice == 4:
            update_task()
        elif choice == 5:
            remove_task()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
