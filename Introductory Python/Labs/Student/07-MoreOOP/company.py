from datetime import datetime


class Employee:

    # Class variables.
    __minimumSalary = 12000
    __nextEmployeeID = 0

    # Initialization.
    def __init__(self, name, salary):
        self.__name = name
        self._salary = max(salary, Employee.__minimumSalary)
        self.__joined = datetime.now()

        self.__id = Employee.__nextEmployeeID
        Employee.__nextEmployeeID += 1

    # Business methods.

    def payRaise(self, amount):
        self._salary += amount

    def payBonus(self, percentBonus=1, min=None, max=None):
        if (min is None or self._salary >= min) and \
           (max is None or self._salary <= max):
            self._salary *= 1 + percentBonus / 100

    def toString(self):
        return "[{0}] {1} earns {2}, joined {3}".format(self.__id, self.__name, self._salary, self.__joined.strftime("%c"))

    # Class methods.

    def getMinimumSalary():
        return Employee.__minimumSalary

    def setMinimumSalary(s):
        Employee.__minimumSalary = s


class Programmer(Employee):

    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.__name = name
        self.__languages = {}

    def set_languages(self, languages):
        self.__languages = languages

    def payBonus(self, percentBonus=1, min=None, max=None):
        if len(self.__languages) > 1:
            self._salary = (self._salary * (1 + percentBonus / 100)) + 100
            return self._salary
        else:
            self._salary *= 1 + percentBonus / 100
            return self._salary

    def toStringTwo(self):
        return f"{self.__name} knows {self.__languages}"
