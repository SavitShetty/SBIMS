from modules.student_model import Student
from modules.storage import save_student, load_students

def add_student():
    print("Enter student details:")

    sid = input("ID: ")
    name = input("Name: ")
    branch = input("Branch: ")
    year = int(input("Year: "))
    gpa = float(input("GPA: "))
    email = input("Email: ")

    s = Student(sid, name, branch, year, gpa, email)
    save_student(s)
    print("Student added successfully!")

def list_students():
    students = load_students()
    if not students:
        print("No students found.")
        return

    print("\n--- All Students ---")
    for stu in students:
        print(stu.sid, stu.name, stu.branch)

from modules.storage import load_students, save_student
import csv

CSV_FILE = "data/students.csv"

def delete_student(sid):
    students = load_students()
    new_list = [s for s in students if s.sid != sid]

    if len(new_list) == len(students):
        print("No student found with that ID.")
        return

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "branch", "year", "gpa", "email"])
        for s in new_list:
            writer.writerow(s.to_list())

    print("Student deleted successfully!")


def update_student(sid):
    students = load_students()
    found = False

    for s in students:
        if s.sid == sid:
            found = True
            print("Leave blank if you do not want to change a field.")

            name = input(f"Name ({s.name}): ") or s.name
            branch = input(f"Branch ({s.branch}): ") or s.branch
            year = input(f"Year ({s.year}): ")
            gpa = input(f"GPA ({s.gpa}): ")
            email = input(f"Email ({s.email}): ") or s.email

            s.name = name
            s.branch = branch
            s.year = int(year) if year else s.year
            s.gpa = float(gpa) if gpa else s.gpa
            s.email = email
            break

    if not found:
        print("No student found with that ID.")
        return

    # rewrite file
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "branch", "year", "gpa", "email"])
        for s in students:
            writer.writerow(s.to_list())

    print("Student updated successfully!")