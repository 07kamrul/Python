result = None

x = int(input("Number 1: "))
y = int(input("Number 2: "))

try:
    result = x / y
except Exception as e:
    print(e)
# except TypeError as e:
#     print("Inside TypeError: ",e)
# except ZeroDivisionError as e:
#     print("Inside ZeroDivisionError: ",e)

print("-- New Line --")
print("Result = ",result)


#Error type
# 1. ZeroDivisionError
# 2. TypeError
