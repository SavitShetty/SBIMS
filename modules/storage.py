import csv
from .student_model import Student

CSV_FILE = "data/students.csv"

def save_student(student):
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(student.to_list())

def load_students():
    students = []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            if row:
                s = Student(row[0], row[1], row[2], int(row[3]), float(row[4]), row[5])
                students.append(s)
    return students