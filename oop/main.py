class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(emp_1.first, emp_1.last)

    def apply_raise(self):
        self.pay = int(float(self.pay) * self.raise_amount)

print(Employee.num_of_emps)

emp_1 = Employee("Benjamin", "McGregor", "50000")
emp_2 = Employee("Test", "Tester", "60000")

print(Employee.num_of_emps)