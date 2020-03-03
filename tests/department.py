from oneperson import Person
from oneperson import Manager 

bob = Person('Bob Simit')
sue = Person('Sue Jones', job='dev', pay=1000)
tom = Manager('Tom, Jones', 5000)

class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)

development = Department(bob, sue)
development.addMember(tom)
development.giveRaises(.10)
development.showAll()
