# To-Do List Application

def display_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nYour To-Do List is empty.")

def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice == 1:
                display_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                remove_task(tasks)
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()
