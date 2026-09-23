tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task done")
    print("4. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({"task": task, "done": False})
        print(tasks)
    elif choice == "2":
         for i, t in enumerate(tasks):
            status = "✓" if t["done"] else " "
            print(f"{i+1}. [{status}] {t['task']}")
    elif choice == "3":
        for i, t in enumerate(tasks):
            status = "✓" if t["done"] else " "
            print(f"{i+1}. [{status}] {t['task']}")
        num = int(input("Which task number is done? "))
        tasks[num -1]["done"] = True
    elif choice == "4":
        print("Goodbye! ")
        break
    