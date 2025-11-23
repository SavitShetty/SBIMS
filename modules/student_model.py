class Student:
    def __init__(self, sid, name, branch, year, gpa, email):
        self.sid = sid
        self.name = name
        self.branch = branch
        self.year = year
        self.gpa = gpa
        self.email = email

    def to_list(self):
        return [self.sid, self.name, self.branch, self.year, self.gpa, self.email]