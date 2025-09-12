
myList = []
while True:
    print("1. Append:")
    print("2. Remove:")
    print("3. Replace:")
    print("4. Sort")
    print("5. Reverse")
    print("6. Print")
    print("7. Quit")
    option = input("Select function:")

    if option == "1":
        myList.append(int(input("Enter value:")))

    elif option == "2":
        myList.remove(int(input("Enter value:")))

    elif option == "3":
        x = int(input("Enter placement of value to be replaced:"))
        new_element = int(input("Enter replacement value:"))
        myList[x] = new_element

    elif option == "4":
        myList.sort()

    elif option == "5":
        myList.reverse()

    elif option == "6":
        print(myList)

    elif option == "7":
        break