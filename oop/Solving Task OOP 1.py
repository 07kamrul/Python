n = input("Name: ")
a = int(input("Age: "))
m = int(input("Marks: "))

class Student:
    def __init__(self,n,a,m):
        self.name = n
        self.age = a
        self.marks = m

    def display(self):
        print("Hi", self.name)
        print("Your age",self.age)
        print("Your marks",self.marks)

s1 = Student(n,a,m)
s1.display()