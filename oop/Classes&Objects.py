class Student:
    #Attribute or variable
    def __init__(self):
        self.name = "Python"
        self.age = 20
        self.marks = 95
        #print("__init__ is called!")

    #Action or method
    def talk(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Marks: ",self.marks)

s1 = Student()
s2 = Student()
s1.talk()
s1.name = "Java"
print(s1.name)
print(s2.name)