from company import Employee
from company import Programmer

# Create some employees and display them.
emp1 = Employee("Bill", 15000)
emp2 = Employee("Ben", 10000)
graham = Programmer("Graham", 20000)
emp3 = Programmer("Dan", 21000)
print(emp1.toString())
print(emp2.toString())
print(emp3.toString())
print(graham.toString())
print(emp2.payBonus())

# graham.set_languages({"Python": 1})
# graham.set_name("Graham")
graham.set_languages({"Pyton": 2, "Java": 2})
# print(graham.toStringTwo())
print(graham.payBonus())
