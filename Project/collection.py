print("\nWelcome to the student data organizer!!")

students = {}

def add_student():
    sid = input("Enter Student ID : ")
    name = input("Enter Name : ")
    age = input("Enter Age : ")
    grade = input("Enter Grade : ")
    subjects = input("Enter Subjects (comma-separated) : ").split(',')
    bod = [" yyyy-mm-dd : "]
    students[sid] = {"Name": name, "Age": age, "Grade": grade, "Subjects": subjects}
    print("Student added successfully!\n")

def display_all():
    print("\n--- All Students ---")
    if not students:
        print("No student records found.\n")
    else:
        for sid, data in students.items():
            print(f"ID: {sid} | Name: {data['Name']} | Age: {data['Age']} | Grade: {data['Grade']} | Subjects: {', '.join(data['Subjects'])}")
    print()

def update_student():
    sid = input("Enter Student ID to update: ")
    if sid in students:
        name = input("Enter new Name : ")
        age = input("Enter new Age : ")
        grade = input("Enter new Grade : ")
        subjects = input("Enter new Subjects (comma-separated) : ").split(',')
        students[sid] = {"Name": name, "Age": age, "Grade": grade, "Subjects": subjects}
        print("Student updated successfully!\n")
    else:
        print("Student ID not found!\n")

def delete_student():
    sid = input("Enter Student ID to delete : ")
    if sid in students:
        del students[sid]
        print("Student deleted successfully!\n")
    else:
        print("Student ID not found!\n")

def display_subjects():
    all_subjects = set()
    for data in students.values():
        all_subjects.update(data["Subjects"])
    print("\n--- Subjects Offered ---")
    print(", ".join(all_subjects) if all_subjects else "No subjects available.")
    print()

# Main menu
while True:
    print("\nSelect an option : ")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice [1 - 6]: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            display_all()
        elif choice == 3:
            update_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            display_subjects()
        elif choice == 6:
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please select between 1 to 6.")
    except ValueError:
        print("Please enter a valid number.")



