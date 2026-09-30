def deadline_tracker():
    deadlines = []
    deadline = int(input("enter the number of deadlines:"))
    for i in range(deadline):
        deadline = input("upcoming deadline or task:")
        date = input("date:")
        priority = input("priority level:")
        deadlines.append({"deadline":deadline,"date":date,"priority":priority})

    print("Your Deadlines:")
    for items in deadlines:
        print(items["deadline"], items["date"], items["priority"])