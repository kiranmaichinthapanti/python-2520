# Initializing Parent Attributes with super()

class Emp:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class fun(Emp):
    def __init__(self, id, name, email):
        super().__init__(id, name)   #Calls Emp’s __init__
        self.email = email

obj = fun(101, "Olivia", "olivia@email.com")
print(obj.id, obj.name, obj.email)

# Emp is the parent class with attributes id and name.
# fun inherits from Emp and adds an email attribute.
# super().__init__(id, name) initializes the parent attributes without rewriting the constructor.

# Issue with not using super()

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Emp(Person):
    def __init__(self, name, id):
        self.name_ = name   # Forgot to call Person’s __init__

emp = Emp("Jack", 103)
#print(emp.name)

# Fixing above error with super()
class Person:  
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Emp(Person):  
    def __init__(self, name, id):
        super().__init__(name, id) 

emp = Emp("James", 103)
print(emp.name, emp.id)

# Emp overrides the constructor of Person.
# super().__init__(name, id) calls the parent constructor to initialize inherited attributes.
# Creating emp = Emp("James", 103) sets both parent and child attributes correctly.

class Mammal:
    def __init__(self, name):
        print(name, "is a mammal")

class CanFly(Mammal):
    def __init__(self, name):
        print(name, "cannot fly")
        super().__init__(name)

class CanSwim(CanFly):
    def __init__(self, name):
        print(name, "cannot swim")
        super().__init__(name)

class Animal(CanSwim):
    def __init__(self, name):
        super().__init__(name)

dog = Animal("Dog")

# Each class calls super().__init__() to ensure parent constructors run.
# Execution follows the hierarchy: Animal → CanSwim → CanFly → Mammal.
# This ensures each parent constructor runs once in the correct order.