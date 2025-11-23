from modules.storage import load_students

def search_by_name(name_part):
    students = load_students()
    result = []

    for stu in students:
        if name_part.lower() in stu.name.lower():
            result.append(stu)

    return result


def filter_by_branch(branch):
    students = load_students()
    result = []

    for stu in students:
        if stu.branch.lower() == branch.lower():
            result.append(stu)

    return result


def top_n_students(n):
    students = load_students()
    students_sorted = sorted(students, key=lambda s: s.gpa, reverse=True)
    return students_sorted[:n]