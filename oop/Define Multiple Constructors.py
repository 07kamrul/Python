class Student:
    def __init__(self):
        print("1st __init__ method.")

    def __init__(self):
        print("2nd __init__ method.")

    def display(self):
        print("Hi")

s1 = Student()
s1.display()