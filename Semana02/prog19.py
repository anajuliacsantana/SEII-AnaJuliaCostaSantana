

class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return'({},{},${})'.format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee('Carl',37,70000)
e2 = Employee('Sarah',29,80000)
e3 = Employee('John',43,90000)

employees = [e1,e2,e3]

# def e_sort(emp):
#     return emp.salary
#     #You can chhose, .name, .age, .salary

s_employees = sorted(employees, key = attrgetter('age'))

print(s_employees)
