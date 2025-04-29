#q7
stack = []
while True:
    print("\n menu:")
    print("1. Push")
    print("2. pop")
    print("3. Display stack")
    print("4. exit")
    choice = int (input("enter you choice:"))

    if choice == 1:
        item = input("enter the item to push:")
        stack.append(item)
        print(f"{item} pushed to stack.")
    elif choice == 2:
        if stack:
            print(f" {stack.pop()} popped from stack.")
        else:
            print("stack is empty")
    elif choice == 3:
        print("stack:",stack)
    elif choice == 4:
        break
    else:
        print("invalid choice!")
