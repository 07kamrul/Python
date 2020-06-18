#Multiple Arguments

def std(name,clas,*marks):
    print("Name: ",name)
    print("Class: ",clas)
    # print("Marks: ",marks)
    for x in marks:
        print("Makrs: ",x)

std("Kamrul",10,90,99,98)