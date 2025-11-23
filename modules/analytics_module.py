from modules.storage import load_students

def branch_distribution():
    students = load_students()
    distro = {}

    for stu in students:
        if stu.branch not in distro:
            distro[stu.branch] = 0
        distro[stu.branch] += 1

    return distro


def average_gpa_by_branch():
    students = load_students()
    totals = {}
    counts = {}

    for stu in students:
        branch = stu.branch

        if branch not in totals:
            totals[branch] = 0
            counts[branch] = 0

        totals[branch] += stu.gpa
        counts[branch] += 1

    averages = {}
    for branch in totals:
        averages[branch] = totals[branch] / counts[branch]

    return averages