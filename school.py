class School():
    def __init__(self, name, roster = {}):
        self.name = name
        self.roster = roster

    def add_student(self, student, grade):
        if self.roster.get(grade):
            self.roster[grade].append(student)
        else:
            self.roster[grade] = [student]
        