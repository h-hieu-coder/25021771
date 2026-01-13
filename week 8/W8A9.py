class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, subject, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)

    def rank(self):
        a = self.avg()
        if a >= 8:
            return "Excellent"
        elif a >= 6.5:
            return "Good"
        elif a >= 5:
            return "Average"
        else:
            return "Poor"


name = input()
student = Student(name)

n = int(input())
while n > 0 :
    subject, score = input().split()
    student.add_score(subject, float(score))
    n -= 1
    
print(f"{student.name} {student.avg():.2f} {student.rank()}")
