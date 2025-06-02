todo_list = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter your task: ")
        todo_list.append(task)
        print("Task added!")
    elif choice == '2':
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
