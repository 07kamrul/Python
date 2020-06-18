class Student:
    def __init__(self,n,a,**m):
        self.name = n
        self.age = a
        self.marks = m

    def display(self):
        print("Hi", self.name)
        print("Your age",self.age)
        print("Your marks",self.marks)

# s1 = Student("Python",22,98,65,97)
s1 = Student("Python",22, Math = 98, Religion = 65, Social= 97)

s1.display()