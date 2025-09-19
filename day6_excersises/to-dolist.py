tasks =[]

def add_task(task):
    tasks.append(task)
    print(f"task added:{task}")
def view_tasks():
    if not tasks:
        print("no tasks.")
    else:
        print("\n---todo list")
        for i,task in enumerate(tasks, start=1):
            print(f"{i},{task}")
def remove_task(index):
    if 0<=index<len(tasks):
        removed = tasks.pop(index)
        print(f"removed:{removed}")
    else:
        print("invalid task number")


while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        task = input("Enter new task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        if tasks:
            try:
                index = int(input("Enter task number to remove: ")) - 1
                remove_task(index)
            except ValueError:
                print("Please enter a valid number.")
    elif choice == "4":
        print("Exiting To-Do List. Bye 👋")
        break
    else:
        print("Invalid choice, please try again.")