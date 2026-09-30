def todo_tracker():
    tasks = []
    count = int(input("number of tasks:"))
    for i in range(count):
        task = input("task:")
        priority = input("priority:")
        status = input("Is it completed?")
        tasks.append({"task":task,"priority":priority,"status":status})
    print("Your To-Do List :")
    for items in tasks:
        print(items["task"],items["priority"],items["status"])
