while True:
    name = input("\nEnter student name (or type Exit to quit): ")

    if name == "Exit":
        print("Goodbye!")
        break

    mark1 = float(input("Enter mark 1: "))
    mark2 = float(input("Enter mark 2: "))
    mark3 = float(input("Enter mark 3: "))

    average = (mark1 + mark2 + mark3) / 3

    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    print("------------------------------")
    print(f"Name   : {name}")
    print(f"Average: {average:.1f}")
    print(f"Grade  : {grade}")
    print("------------------------------")