FILENAME = "student.txt"
while True:
    print("\n" + "=" * 40)
    print("    STUDENT RECORD FILE SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Save Student Records")
    print("5. Exit")
    print("=" * 40)
    try:
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            try:
                roll = input("Enter Roll Number: ").strip()
                file = open(FILENAME, "r")
                line = file.readline()
                found = False
                while line:
                    data = line.strip().split("|")
                    if len(data) == 3 and data[0] == roll:
                        found = True
                        break
                    line = file.readline()
                file.close()
                if found:
                    print("Error: Roll number already exists!")
                    continue
            except FileNotFoundError:
                pass
            try:
                name = input("Enter Student Name: ").strip()
                marks = float(input("Enter Marks: "))
                if not roll or not name:
                    raise ValueError("Fields cannot be empty.")
                if marks < 0 or marks > 100:
                    raise ValueError("Marks must be between 0 and 100.")
                file = open(FILENAME, "a")
                file.write(roll + "|" + name + "|" + str(marks) + "\n")
                file.close()
                print("Student added successfully!")
            except ValueError as error:
                print("Invalid input:", error)
            except OSError as error:
                print("File error:", error)
        elif choice == 2:
            try:
                file = open(FILENAME, "r")
                print("\n" + "-" * 50)
                print(f"{'Roll No.':<15}{'Name':<20}{'Marks':>10}")
                print("-" * 50)
                line = file.readline()
                count = 0
                while line:
                    data = line.strip().split("|")
                    if len(data) == 3:
                        print(f"{data[0]:<15}{data[1]:<20}{data[2]:>10}")
                        count += 1
                    line = file.readline()
                file.close()
                print("-" * 50)
                print("Total Students:", count)
            except FileNotFoundError:
                print("No student records found.")
            except OSError as error:
                print("File error:", error)
        elif choice == 3:
            roll = input("Enter Roll Number to Search: ").strip()
            try:
                file = open(FILENAME, "r")
                line = file.readline()
                found = False
                while line:
                    data = line.strip().split("|")
                    if len(data) == 3 and data[0] == roll:
                        print("\nSTUDENT FOUND")
                        print("Roll Number:", data[0])
                        print("Name:", data[1])
                        print("Marks:", data[2])
                        found = True
                        break
                    line = file.readline()
                file.close()
                if not found:
                    print("Student record not found.")
            except FileNotFoundError:
                print("Student file does not exist.")
            except OSError as error:
                print("File error:", error)
        elif choice == 4:
            try:
                file = open(FILENAME, "r")
                records = file.readlines()
                file.close()
                file = open(FILENAME, "w")
                file.writelines(records)
                file.close()
                print("Student records saved successfully!")
                print("Total records saved:", len(records))
            except FileNotFoundError:
                print("No records available to save.")
            except OSError as error:
                print("File error:", error)
        elif choice == 5:
            print("Thank you for using Student Record System.")
            break
        else:
            print("Invalid choice! Enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input! Please enter an integer.")
