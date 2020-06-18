def std(name,cls,**marks):
    print("Name: ",name)
    print("Class: ",cls)
    # Key
    # for x in marks:
    #     print("Marks: ",x)

    # key with value
    for x,y in marks.items():
        print(x + " Marks: ",y)

std(name="Kamrul",cls=10, english =90,bangla=98,math=99)