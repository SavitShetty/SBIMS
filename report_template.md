Student Branch Information Management System (SBIMS)

Author: Savit Shetty
University: VIT Bhopal
Course: CSE – Build Your Own Project
Year: 2025

INTRODUCTION:

In modern educational institutions, efficient management of student data is essential. Large numbers of students spread across different branches make manual record-keeping difficult, error-prone, and time-consuming.

This project, Student Branch Information Management System (SBIMS), is a modular Python application designed to simplify and streamline the management of student information using a command-line interface and CSV-based storage.

PROBLEM STATEMENT:

Manual management of student records becomes increasingly challenging as student numbers grow. Information such as name, branch, year, GPA, and email is scattered or stored in unstructured formats, making operations like searching, sorting, updating, and analyzing tedious and inefficient.

SBIMS aims to solve these issues by offering a centralized digital management system with CRUD operations and basic analytics

OBJECTIVES:

To develop a modular and scalable system for managing student data

To implement CRUD operations on student records

To provide easy search, filter, and analytical functionalities

To ensure a user-friendly interaction through a command-line menu

To demonstrate clean Python coding practices and modular structure.


FUNCTIONAL REQUIREMENT:

The system provides the following functionalities:

Add Student – Add a new student record

List Students – Display all students

Search by Name – Partial match search across names

Filter by Branch – Display only students belonging to a specific branch

Top N Students – View highest-GPA students

Update Student – Modify existing student information

Delete Student – Remove a student by ID

Branch Distribution – Number of students per branch

Average GPA per Branch – Compute branch-wise GPA averages

NON FUNCTIONAL REQUIREMENT:

Usability: Simple text-based interface

Maintainability: Modular file structure (input, process, analytics, model, storage)

Performance: CSV operations optimized with minimal overhead

Scalability: New modules or analytics can be added easily

Reliability: Validations to prevent invalid entries

Portability: Runs on any system with Python installed



ARCHITECTURE:

User
  ↓
Main Menu (main.py)
  ↓
Modules
  ↓
CSV Storage (students.csv)

MODULES:

student_model.py → Defines Student class

storage.py → Read/write CSV

input_module.py → Add/List/Update/Delete

process_module.py → Search/Filter/Top N

analytics_module.py → Distribution & GPA stats

        
 Diagram

             Admin     
               |
    
  |     |      |        |       |
 Add   List  Search  Filter Analytics


WORKFLOW:
Start → Show Menu → Get Input → Perform Operation → Back to Menu → Exit

SEQUENCE:
User → main.py → input_module → storage → CSV File  


CLASS DIAGRAM:
Student
 ├── sid
 ├── name
 ├── branch
 ├── year
 ├── gpa
 └── email

Conclusion

SBIMS successfully demonstrates a modular student management system capable of handling core academic data operations effectively.
It meets all the functional and non-functional requirements described in the assignment and provides a strong foundation for further extension.