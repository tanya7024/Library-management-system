from jsonfile_manager import *


def student_register():
    students = load_data()
    ID = input("Enter a Student ID: ")

    if ID in students:
        print("Student already registered!")
        print("Try Another ID")
        return

    name = input("Enter Student Name: ")
    department = input("Enter Student Department: ")
    contact = int(input("Enter Student Contact Number: "))

    students[ID] = {
        "Student_ID": ID,
        "Student_Name": name,
        "Student_Department": department,
        "Student_Contact": contact
    }
    add_data(students)
    print("Student details added successfully!")