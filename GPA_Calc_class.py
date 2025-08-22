class course:
    #attributes
    def __init__(self, grade, credit):
       self.grades = grade
       self.credit = credit
       
class calc:
    #attributes 
    def __init__(self, grades):
        self.grades = grades
        self.courses = []

    def add_course(self, grade, credits):
        if grade not in self.grades:
            raise ValueError(f"Invalid grade '{grade}' entered.")
        self.courses.append(course(grade, credits))

    def calculator_gpa(self):
        total_points = 0
        total_credits = 0
        for course in self.courses:
            total_points += self.grades[course.grades] * course.credit
            total_credits += course.credit
        if total_credits == 0:
            return 0
        return total_points / total_credits
    
    def gpa_to_letter(self, gpa):
        if gpa >= 4.0:
            return "A"
        elif gpa >= 3.7:
            return "A-"
        elif gpa >= 3.3:
            return "B+"
        elif gpa >= 3.0:
            return "B"
        elif gpa >= 2.7:
            return "B-"
        elif gpa >= 2.3:
            return "C+"
        elif gpa >= 2.0:
            return "C"
        elif gpa >= 1.7:
            return "C-"
        elif gpa >= 1.3:
            return "D+"
        elif gpa >= 1.0:
            return "D"
        else:
            return "F"