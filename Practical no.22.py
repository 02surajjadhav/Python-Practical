import json
import os
FILE_NAME = "students.json"
def load_students():
    """Load student records from JSON file."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Student data file is corrupted. Starting with empty records.")
        return []
    except Exception as error:
        print("Unexpected error while loading data:", error)
        return []
def save_students(students):
    """Save student records to JSON file."""
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
    except PermissionError:
        print("Error: Permission denied while saving data.")
    except Exception as error:
        print("Unexpected error while saving data:", error)
def get_integer_input(message):
    """Take integer input safely."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
def get_float_input(message):
    """Take float input safely."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
def add_student(students):
    """Add a new student record."""
    try:
        roll_no = get_integer_input("Enter Roll Number: ")
        for student in students:
            if student["roll_no"] == roll_no:
                print("Student with this roll number already exists!")
                return
        name = input("Enter Student Name: ").strip()
        course = input("Enter Course: ").strip()
        if name == "" or course == "":
            print("Name and course cannot be empty.")
            return
        marks = get_float_input("Enter Marks (0-100): ")
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return
        student = {
            "roll_no": roll_no,
            "name": name,
            "course": course,
            "marks": marks
        }
        students.append(student)
        save_students(students)
        print("Student added successfully!")
    except Exception as error:
        print("Error while adding student:", error
def view_students(students):
    """Display all student records."""
    if not students:
        print("No student records found.")
        return
    print("\n---------------- STUDENT RECORDS ----------------")
    print(f"{'Roll No':<10}{'Name':<20}{'Course':<15}{'Marks':<10}")
    print("-" * 55)
    for student in students:
        print(f"{student['roll_no']:<10}{student['name']:<20}"
              f"{student['course']:<15}{student['marks']:<10}")
    print("-" * 55)
    print("Total Students:", len(students))
def search_student(students):
    """Search a student by roll number."""
    try:
        roll_no = get_integer_input("Enter Roll Number to search: ")
        for student in students:
            if student["roll_no"] == roll_no:
                print("\nStudent Found:")
                print("Roll Number :", student["roll_no"])
                print("Name        :", student["name"])
                print("Course      :", student["course"])
                print("Marks       :", student["marks"])
                return
        print("Student not found.")
    except Exception as error:
        print("Error while searching student:", error)
def update_student(students):
    """Update marks of an existing student."""
    try:
        roll_no = get_integer_input("Enter Roll Number to update: ")
        for student in students:
            if student["roll_no"] == roll_no:
                print("Current Marks:", student["marks"])
                new_marks = get_float_input("Enter New Marks (0-100): ")
                if new_marks < 0 or new_marks > 100:
                    print("Marks must be between 0 and 100.")
                    return
                student["marks"] = new_marks
                save_students(students)
                print("Student record updated successfully!")
                return
        print("Student not found.")
    except Exception as error:
        print("Error while updating student:", error)
def delete_student(students):
    """Delete a student record."""
    try:
        roll_no = get_integer_input("Enter Roll Number to delete: ")
        for student in students:
            if student["roll_no"] == roll_no:
                students.remove(student)
                save_students(students)
                print("Student record deleted successfully!")
                return
        print("Student not found.")
    except Exception as error:
        print("Error while deleting student:", error)
def show_statistics(students):
    """Show total students, average marks, highest and lowest marks."""
    if not students:
        print("No student records available.")
        return
    marks_list = [student["marks"] for student in students]
    print("\n---------------- STATISTICS ----------------")
    print("Total Students :", len(students))
    print("Average Marks  :", round(sum(marks_list) / len(marks_list), 2))
    print("Highest Marks  :", max(marks_list))
    print("Lowest Marks   :", min(marks_list))
    print("---------------------------------------------")
def main():
    students = load_students()
    while True:
        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Show Statistics")
        print("7. Exit")
        print("===============================================")
        choice = input("Enter your choice (1-7): ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            show_statistics(students)
        elif choice == "7":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice! Please select between 1 and 7.")

if __name__ == "__main__":
    main()
