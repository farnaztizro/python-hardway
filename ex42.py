# Animal is-a object
class Animal(object):
    pass

# Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        self.name = name

# Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        # Person has-a name
        self.name = name
        # Person has-a pet
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):  
        super(Employee, name).__init__(name)   
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

# Mary has-a Pet and her Pet has-a name satan
mary.pet = satan

frank = Employee("Frank", 2000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
