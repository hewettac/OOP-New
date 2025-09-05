
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    option = input("Select an operation option:")

    if option =="1":
        n1 = int(input("Enter number 1:"))
        n2 = int(input("Enter number 2:"))
        print("The answer is:", n1 + n2)

    elif option == "2":
        n1 = int(input("Enter number 1:"))
        n2 = int(input("Enter number 2:"))
        print("The answer is:", n1 - n2)

    elif option == "3":
        n1 = int(input("Enter number 1:"))
        n2 = int(input("Enter number 2:"))
        print("The answer is:", n1 * n2)

    elif option == "4":
        n1 = int(input("Enter number 1:"))
        n2 = int(input("Enter number 2:"))
        print("The answer is:", n1 / n2)


    elif option == "5":
        break