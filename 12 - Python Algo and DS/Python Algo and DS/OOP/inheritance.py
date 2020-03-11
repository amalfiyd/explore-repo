'''
Example of inheritance in python
'''
# Parent class, i.e. Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def whoami(self):
        print("My name is ", self.name, ". I am ", self.age, ' years old.')

class Job(Person):
    def __init__(self, name, age, job):
        self.job = job
        Person.__init__(self, name, age)

    def myProfile(self):
        print("My name is ", self.name, ". I am ", self.age, ' years old. I am doing ', self.job)


me = Job("Amalfi", 30, "Data Scientist")
me.myProfile()

