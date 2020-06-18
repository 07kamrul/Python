class Python:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __sub__(self, other):
        return self.pages - other.pages

class Java:
    def __init__(self,pages):
        self.pages = pages

b1 = Python(380)
b2 = Java(480)

print(b1 + b2)
print(b1 > b2)
print(b1 - b2)

