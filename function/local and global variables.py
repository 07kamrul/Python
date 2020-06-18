x = 10
y = 20

def sum(x,y):
    global z
    z = 50
    print(x)
    print(y)
    print(z)

sum(x,y)
print("------")
print(x)
print(y)
print(z)
