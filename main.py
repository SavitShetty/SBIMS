# main.py (full menu)
from modules.input_module import add_student, list_students, update_student, delete_student
from modules.process_module import search_by_name, filter_by_branch, top_n_students
from modules.analytics_module import branch_distribution, average_gpa_by_branch

def print_menu():
    print("\nSBIMS - Menu")
    print("1. Add student")
    print("2. List students")
    print("3. Search student by name")
    print("4. Filter by branch")
    print("5. Top N students by GPA")
    print("6. Branch distribution")
    print("7. Average GPA by branch")
    print("8. Update student")
    print("9. Delete student")
    print("0. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            name = input("Enter name (or part): ").strip()
            if name:
                results = search_by_name(name)
                if results:
                    print("\n--- Search Results ---")
                    for s in results:
                        print(s.sid, s.name, s.branch, s.year, s.gpa, s.email)
                else:
                    print("No students found.")
            else:
                print("No input provided.")
        elif choice == "4":
            branch = input("Enter branch: ").strip()
            if branch:
                results = filter_by_branch(branch)
                if results:
                    print(f"\n--- Students in {branch} ---")
                    for s in results:
                        print(s.sid, s.name, s.year, s.gpa, s.email)
                else:
                    print("No students found in that branch.")
            else:
                print("No branch provided.")
        elif choice == "5":
            n = input("Enter N: ").strip()
            if n.isdigit():
                results = top_n_students(int(n))
                if results:
                    print(f"\n--- Top {n} Students by GPA ---")
                    for s in results:
                        print(s.sid, s.name, s.branch, s.gpa)
                else:
                    print("No students available.")
            else:
                print("Please enter a valid number.")
        elif choice == "6":
            d = branch_distribution()
            if d:
                print("\n--- Branch distribution ---")
                for branch, count in d.items():
                    print(f"{branch} : {count}")
            else:
                print("No students found.")
        elif choice == "7":
            avgs = average_gpa_by_branch()
            if avgs:
                print("\n--- Average GPA by Branch ---")
                for branch, avg in avgs.items():
                    print(f"{branch} : {round(avg, 2)}")
            else:
                print("No students found.")
        elif choice == "8":
            sid = input("Enter ID to update: ").strip()
            if sid:
                update_student(sid)
            else:
                print("No ID provided.")
        elif choice == "9":
            sid = input("Enter ID to delete: ").strip()
            if sid:
                delete_student(sid)
            else:
                print("No ID provided.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()