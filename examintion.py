
class examination:
    def __init__(self, student, score):
        self.student = student
        self.score = score

    def CalculateGrade(self):
        if self.score >= 50:
            self.grade = "A"
        else:
            self.grade = "B"
    
    def CalculatePercentage(self):
        self.percentage = round((self.score/60 * 100),1)
        
    
    def ShowStudentData(self):
        print(f"{self.student} scored {self.score}/60 or {self.percentage} which is a grade {self.grade}")



student1 = examination("Alex", 56)
student2 = examination("John", 47)

student1.CalculateGrade()
student2.CalculateGrade()

student1.CalculatePercentage()
student2.CalculatePercentage()

student1.ShowStudentData()
student2.ShowStudentData()