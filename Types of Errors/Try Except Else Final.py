result = None

x = int(input("Number 1: "))
y = int(input("Number 2: "))

try:
    result = x / y

except Exception as e:
    print(e)

else:
    print("Inside Else")

finally:
    print("Inside Finally")

print("--- New Line ---")
print("Result = ",result)
