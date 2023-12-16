from company import Employee
from company import Programmer

# Create some employees and display them.
emp1 = Employee("Bill", 15000)
emp2 = Employee("Ben", 20000)
graham = Programmer("Graham", 30000)
emp3 = Programmer("Bob", 21000)
print(emp1.toString())
print(emp2.toString())
print(graham.toString())
print(emp3.toString())
graham.get_languages("Graham", {"Python": "Level - 1"})
emp3.get_languages("Bob", {"Java": 1})
