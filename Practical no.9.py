student_names = []
student_marks = []

while True:
    print("=" * 40)
    print("     STUDENT MARKS MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Insert Student Record")
    print("2. Delete Student Record")
    print("3. Update Student Marks")
    print("4. Traverse / Display All Records")
    print("5. Search Student")
    print("6. Show Statistics")
    print("7. Exit")
    print("=" * 40)

    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip()

        if name in student_names:
            print(f"Student '{name}' already exists! Use update option instead.\n")
        else:
            marks = float(input(f"Enter marks for {name}: "))
            student_names.append(name)
            student_marks.append(marks)
            print(f"Record for '{name}' inserted successfully.\n")

    elif choice == "2":
        name = input("Enter student name to delete: ").strip()

        if name in student_names:
            index = student_names.index(name)
            student_names.pop(index)
            student_marks.pop(index)
            print(f"Record for '{name}' deleted successfully.\n")
        else:
            print(f"Student '{name}' not found.\n")

    elif choice == "3":
        name = input("Enter student name to update: ").strip()

        if name in student_names:
            index = student_names.index(name)
            new_marks = float(input(f"Enter new marks for {name}: "))
            student_marks[index] = new_marks
            print(f"Marks for '{name}' updated successfully.\n")
        else:
            print(f"Student '{name}' not found.\n")

    elif choice == "4":
        if len(student_names) == 0:
            print("No records to display.\n")
        else:
            print("\n{:<5} {:<20} {:<10}".format("No.", "Name", "Marks"))
            print("-" * 35)

            for i in range(len(student_names)):
                print("{:<5} {:<20} {:<10}".format(
                    i + 1, student_names[i], student_marks[i]
                ))
            print()

    elif choice == "5":
        name = input("Enter student name to search: ").strip()

        if name in student_names:
            index = student_names.index(name)
            print(f"Name: {name}, Marks: {student_marks[index]}\n")
        else:
            print(f"Student '{name}' not found.\n")

    elif choice == "6":
        if len(student_marks) == 0:
            print("No records available for statistics.\n")
        else:
            total = sum(student_marks)
            average = total / len(student_marks)
            highest = max(student_marks)
            lowest = min(student_marks)

            topper_index = student_marks.index(highest)
            weakest_index = student_marks.index(lowest)

            print("\n----- Class Statistics -----")
            print(f"Total Students : {len(student_names)}")
            print(f"Average Marks  : {average:.2f}")
            print(f"Highest Marks  : {highest} (Student: {student_names[topper_index]})")
            print(f"Lowest Marks   : {lowest} (Student: {student_names[weakest_index]})")
            print()

    elif choice == "7":
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.\n")
