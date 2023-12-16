class Employee:
    from datetime import datetime
    __currentDateAndTimeVariable = datetime.now().strftime("%d-%m-%Y")
    __max_range_bonus = 0.2
    __min_range_bonus = 0.1

    def __init__(self, first_name, last_name, salary):

        self.__first_name = first_name
        self.__last_name = last_name
        self.__salary = salary

    def payRaise(self, pay_raise):
        self.pay_raise = pay_raise
        self.__salary += pay_raise

    def setFirstName(self, first_name):
        self.__first_name = first_name

    def getFirstName(self):
        return self.__first_name

    def setLastName(self, last_name):
        self.__last_name = last_name

    def getLastName(self):
        return self.__last_name

    def setSalary(self, salary):
        self.__salary = salary

    def getSalary(self):
        return self.__salary

    # Will need looked at

    # Bonus Without parameters
    # def payBonus(self):
    #     self.bonus = 0.01
    #     self.__salary *= self.bonus
    #     print(f"Your bonus is: {self.__salary}")

    # Will need looked at
    def bonusPayRange(self, bonus):
        self.bonus = bonus
        if bonus in range(40000, 100000):
            print("Not in range")
        elif bonus <= 20000 and bonus < 30000:
            bonus *= Employee.__min_range_bonus
            print(bonus)
        elif bonus > 30000:
            bonus *= Employee.__max_range_bonus
            print(bonus)

    # Will need looked at
    def payBonus(self, bonus_percentage):
        self.bonus_percentage = bonus_percentage
        self.bonus_percentage *= self.__salary
        print(
            f"Your bonus for your £{format(self.__salary,',')} salary  is: £{format(self.bonus_percentage,',')}")

    def toString(self):
        print(
            f"Employee name: {self.__first_name} {self.__last_name}, Salary: {self.__salary}. They joined on {Employee.__currentDateAndTimeVariable}")


graham = Employee("Graham", "Jones", 20000)
graham.toString()
graham.setLastName("McKane")
graham.getLastName()
graham.setSalary(21000)
graham.getSalary()
graham.toString()
graham.payRaise(300)
graham.toString()
graham.payBonus(0.05)
graham.bonusPayRange(35000)
