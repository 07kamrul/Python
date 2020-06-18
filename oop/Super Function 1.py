class Parent:
    def __init__(self,name):
        print("Parent __init__", name)

class Child(Parent):
     def __init__(self):
         print("Child __init__")
         Parent.__init__(self,"Kamrul")

child_obj = Child()