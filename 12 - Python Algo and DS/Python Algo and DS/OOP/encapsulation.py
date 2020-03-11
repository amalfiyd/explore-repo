'''
Encapsulation example with Python
'''

# Parent class
class Employee:
    def __init__(self):
        self.name = "Amalfi"
        self._id = "13507023"
        self.__salary = 10000

    def readSalary(self):
        return self.__salary

# Child class
class ERP:
    def __init__(self):
        Employee.__init__(self)

    def getID(self):
        print(self.name, "'s ID is", self._id)

    def getSalary(self):
        print(self.name, "'s salary is", Employee.readSalary(self))

myERP = ERP()