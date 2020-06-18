class TeaException(Exception):
    def __init__(self,arg):
        self.msg = arg

class Tea:
    def __init__(self,temperature):
        self.__temperature = temperature

    def drink_tea(self):
        if self.__temperature > 85 :
            # print("Hot to drink.")
            raise TeaException("Hot to drink")

        elif self.__temperature < 65:
            # print("Cold to drink.")
            raise TeaException("Cold to drink")
        else:
            print("Normal to drink")

cup = Tea(100)
cup.drink_tea()

