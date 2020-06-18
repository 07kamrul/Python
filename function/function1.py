def sum(inp1,inp2):
    if type(inp1) == type(inp2):
        return inp1 + inp2
    else:
        return  "Datatype are different"

x = sum("10",15)
print(x)

