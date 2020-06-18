class Salary:
    def __init__(self, pay, reward):
        self.pay = pay
        self.reward = reward

    def annual_salary(self):
        return (self.pay * 12) + self.reward

class Employee:
    def __init__(self, name, position, pay, reward):
        self.name = name
        self.position = position
        self.final_salary = Salary(pay,reward)

    def employee_final_salary(self):
        return self.final_salary.annual_salary()

emp = Employee("Kamrul", "Software", 15000, 1000)

print(emp.employee_final_salary())