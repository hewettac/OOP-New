myStudents = {}

while True:
    print("1. Add a Student")
    print("2. Delete a Student")
    print("3. Edit a Student")
    print("4. Print a Student")
    print("5. Quit")
    option = input("Select function:")

    if option == "1":
        SID = input("Enter student ID:")
        Name = input("Enter student name:")
        Lab1 = int(input("Enter Lab 1 grade:"))
        Lab2 = int(input("Enter Lab 2 grade:"))
        Lab3 = int(input("Enter Lab 3 grade:"))
        Lab4 = int(input("Enter Lab 4 grade:"))
        Lab5 = int(input("Enter Lab 5 grade:"))
        Total = int(Lab1+Lab2+Lab3+Lab4+Lab5)
        Percent = int(((Total * 2) / 100) * 100)
        Average = int(Total / 5)
        myStudents.update({SID:{"Name":Name,
                                 "Lab-1":Lab1,
                                 "Lab-2":Lab2,
                                 "Lab-3":Lab3,
                                 "Lab-4":Lab4,
                                "Lab-5":Lab5,
                                "Total Points":Total,
                                "Percent":Percent,
                                "Average Points":Average
                                 }})

    if option == "2":
        del myStudents[input("Enter student ID to be deleted:")]

    if option == "3":
        SID = input("Enter student ID:")
        newName = input("Enter student name:")
        newLab1 = int(input("Enter new Lab 1 grade:"))
        newLab2 = int(input("Enter new Lab 2 grade:"))
        newLab3 = int(input("Enter new Lab 3 grade:"))
        newLab4 = int(input("Enter new Lab 4 grade:"))
        newLab5 = int(input("Enter new Lab 5 grade:"))
        newTotal = int(newLab1 + newLab2 + newLab3 + newLab4 + newLab5)
        newPercent = int(((newTotal * 2) / 100) * 100)
        newAverage = int(newTotal / 5)
        myStudents.update({SID: {"Name": newName,
                                                            "Lab-1": newLab1,
                                                            "Lab-2": newLab2,
                                                            "Lab-3": newLab3,
                                                            "Lab-4": newLab4,
                                                            "Lab-5": newLab5,
                                                            "Total Points":newTotal,
                                                            "Percent":newPercent,
                                                            "Average Points":newAverage
                                                            }})

    if option == "4":
        print(myStudents)
        x = input("Enter student ID to print:")
        print(myStudents[x])

    if option == "5":
        break