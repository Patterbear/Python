import datetime


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(emp_1.first, emp_1.last)

    def apply_raise(self):
        self.pay = int(float(self.pay) * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() > 4:
            return False
        return True


emp_1 = Employee("Benjamin", "McGregor", "50000")
emp_2 = Employee("Test", "Tester", "60000")

my_date = datetime.date(2020, 8, 8)

print(Employee.is_workday(my_date))
