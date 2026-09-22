tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print(tasks)
    elif choice == "2":
        for t in tasks:
            print(t)
    elif choice == "3":
        print("Goodbye! ")
        break