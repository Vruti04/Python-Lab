#q8
queue = []
while True:
    print("\nMenu:")
    print("1. enqueue")
    print("2. dequeue")
    print("3. display queue")
    print("4. exit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        item = input("enter the item to enqueue:")
        queue.append(item)
        print(f" {item} added to queue.")
    elif choice == 2:
        if queue:
            print(f" {queue.pop(0)} removed from queue.")
        else:
            print("queue is empty!")
    elif choice == 3:
        print("queue:", queue)
    elif choice == 4:
        break
    else:
        print("invalid choice!")
