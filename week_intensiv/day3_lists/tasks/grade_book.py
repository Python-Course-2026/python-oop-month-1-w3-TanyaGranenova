class GradeBook:
    """ЗАДАЧА: Найти имя студента с самым высоким средним баллом"""
    def __init__(self): self.students = {} # {"Ivan": [5, 4], "Oleg": [3]}
    def get_best_student(self):
        if len(self.students) == 0:
            return None
        best_student = None
        best_average = -1
        for student, grades in self.students.items():
            if grades:
                average = sum(grades) / len(grades)
                if average > best_average:
                    best_average = average
                    best_student = student
        return best_student




