from company import Employee
from company import Programmer

# Create some employees and display them.
emp1 = Employee("Bill", 15000)
emp2 = Employee("Ben", 20000)
graham = Programmer("Graham", 30000)
emp3 = Programmer("Dan", 21000)
print(emp1.toString())
print(emp2.toString())
print(emp3.toString())

# graham.set_languages({"Python": 1})
graham.set_name("Graham")
graham.set_languages({"Pyton": 2, "Java": 1})
print(graham.toStringTwo())
graham.set_languages({})
print(graham.toStringTwo())
