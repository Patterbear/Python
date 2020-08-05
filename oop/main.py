class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(emp_1.first, emp_1.last)


emp_1 = Employee("Benjamin", "McGregor", "50000")
emp_2 = Employee("Test", "Tester", "60000")

ep_1.fullname()
print(Employee.fullname(emp_1))
# print(emp_2.fullname())