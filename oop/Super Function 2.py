class Parent:
    def __init__(self,name):
        print("Parent __init__", name)

class Parent2:
    def __init__(self,name):
        print("Parent2  __init__", name)

class Child(Parent,Parent2):
     def __init__(self):
         print("Child __init__")
         super().__init__("Kamrul")
         Parent.__init__(self,"Hasan")

child_obj = Child()
print(Child.__mro__)