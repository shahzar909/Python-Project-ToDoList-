tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added to the list.")

def list_tasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("\nCurrent Tasks:")
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index + 1}. {task['task']} [{status}]")

def update_task():
    list_tasks()
    try:
        task_number = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_number < len(tasks):
            task = tasks[task_number]
            print(f"Current task: {task['task']}")
            new_task = input("Enter the updated task: ")
            task["task"] = new_task
            print(f"Task #{task_number + 1} updated to: {new_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def complete_task():
    list_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
            print(f"Task #{task_number + 1} marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def delete_task():
    list_tasks()
    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            print(f"Task '{removed_task['task']}' has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    while True:
        print("\nTo-Do List Application")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Update a task")
        print("4. Mark a task as completed")
        print("5. Delete a task")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
