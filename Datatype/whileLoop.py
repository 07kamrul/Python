x = 0

while x < 6:
    print("Current Value of x",x)
    # x = x + 1
    x +=1
else:
    print("Loop completed")

num = 1
sum = 0
print("Enter number for sum, Press '0' to exit.")
while num != 0:
    num = int(input("Enter Number: "))
    sum = sum + num
else:
    print("Loop Completed.")