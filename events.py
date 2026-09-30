def event_tracker():
    events = {}
    event = int(input("number of events:"))
    for i in range(event):
        event = input("event name:")
        date = input("date:")
        events[event] = date
    print("The Upcoming Events:")
    for output in events:
        print(output,":",events[output])

