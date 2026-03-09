# To-Do List with File Saving

while True:

    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")

        file = open("tasks.txt", "a")
        file.write(task + "\n")
        file.close()

        print("Task saved successfully!")

    elif choice == "2":
        try:
            file = open("tasks.txt", "r")
            tasks = file.readlines()
            file.close()

            if len(tasks) == 0:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for i in range(len(tasks)):
                    print(i+1, ".", tasks[i].strip())

        except FileNotFoundError:
            print("No tasks yet.")

    elif choice == "3":
        print("Exiting To-Do List...")
        break

    else:
        print("Invalid choice!")
