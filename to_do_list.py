

def show_menu():
    print("\nTo-Do List App")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Exit")

def view_tasks(file_name):
    try:
        with open(file_name, "r") as file:
            tasks = file.readlines()
        if tasks:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
        else:
            print("\nYour to-do list is empty.")
    except FileNotFoundError:
        print("\nNo tasks found. Start by adding one!")

def add_task(file_name):
    task = input("Enter the task: ")
    with open(file_name, "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def delete_task(file_name):
    try:
        with open(file_name, "r") as file:
            tasks = file.readlines()
        if not tasks:
            print("Your to-do list is empty.")
            return
        view_tasks(file_name)
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            with open(file_name, "w") as file:
                file.writelines(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks found. Start by adding one!")
    except ValueError:
        print("Please enter a valid number.")

def to_do_list_app():
    file_name = "todo_list.txt"
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(file_name)
        elif choice == "2":
            add_task(file_name)
        elif choice == "3":
            delete_task(file_name)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


to_do_list_app()
