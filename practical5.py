from collections import deque
events = deque()

while True:
    print("\n1. Add event")
    print("n2. Process next event")
    print("n3. Display pending event")
    print("n4. Cancel an event")
    print("n5. Exit")

    ch = int(input("Enter choice:"))

    if ch == 1:
        event = input("Enter event:")
        events.append(event)
        print("Event added successfully.")

    elif ch == 2:
        if events:
            print("Processed event:", events.popleft())
        else:
            print("No events to process.")

    elif ch == 3:
        if events:
            print("Pending events:", list(event))
        else:
            print("No pending events.")

    elif ch == 4:
        event = input("Enter to cancel an event:")
        if event in events:
            print("Event cancelled successfully:")
        else:
            print("Event not found.")

    elif ch == 5:
        print("Exiting....")
        break

    else:
        print("Invalid choice!")