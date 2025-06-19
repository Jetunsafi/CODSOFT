tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit\n")

    choice = input("Choose:")
    if choice == "1":
        task = input("\nEnter Task:")
        tasks.append(task)
        print("Task Added to the List!")
    elif choice == "2":
        print("Your tasks:\n")
        for t in tasks:
            print("~", t)
    elif choice == "3":
        task = input("Enter task to remove:")
        if task in tasks:
            tasks.remove(task)
            print("Task Removed from the List!")
        else:
            print("Task not found!")
    elif choice == "4":
        break
