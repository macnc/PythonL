#! /usr/bin/python
# _*_coding: utf-8


# Animal is-a object (yes, sort of confusing) look at extra credit
class Animal(object):
    pass


# Dog is-a Animal class
class Dog(Animal):
    def __init__(self, name):
        # The dog class has-a name attribute
        self.name = name

    def show_name():
        print self.name


# Cat is-a Animal sub-class
class Cat(Animal):
    # The cat class has-a name attribute
    def __init__(self, name):
        self.name = name


# The person is a object class
class Person(object):
    # The person has-a attribute
    def __init__(self, name):
        self.name = name
        # Person has-a pet of some kind
        self.pep = None


# Employee is-a Person class
class Employee(Person):
    def __init__(self, name, salary):
        '''
        # I don't know about this code, call the father
        # class for initialize name?
        '''
        super(Employee, self).__init__(name)
        # An empolyee has-a salary attribute
        self.salary = salary

    def show_salary(self):
        print self.salary

    def show_detail(self):
        print "This man's name is: %s; and salary is %d" % (self.name,
                                                            self.salary)


# Fish is-a object class
class Fish(object):
    pass


# Salmon is a Fish class
class Salmon(Fish):
    pass


# Halibut is-a Fish class
class Halibut(Fish):
    pass

# rover is-a dog
rover = Dog("Rover")
rover.show_name

# satan is-a cat
satan = Cat("Satan")

# mary is-a person
mary = Person("Mary")

# Mary's pet is satan
mary.pet = satan

# Frank is a Employee with 120000 dollars salary
frank = Employee("Frank", 120000)

# frank's pet is rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
