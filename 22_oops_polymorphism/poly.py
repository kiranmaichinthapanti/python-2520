# method overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self): # Overriding
        print("Dogs makes a Woof")

class Cat(Animal):
    def sound(self): # Overriding
        print("Cats makes a Meow")
    
class Cow(Animal):
    pass

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

cow = Cow()
cow.sound()