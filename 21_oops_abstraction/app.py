# Abstraction

from abc import ABC, abstractmethod

# abstract class
class Laptop(ABC):

    # abstract Methods
    @abstractmethod
    def processor(self):
        pass

    @abstractmethod
    def ram_hdd(self):
        pass

    # concrete method
    def screen_saver(self):
        print("Screen Saver")

# laptop = Laptop() # TypeError: Can't instantiate abstract class
# laptop.processor()

# Implementation
class Lenovo(Laptop):
    def processor(self):
        print("Lenovo Laptop Processor")

    def ram_hdd(self):
        print("Lenovo Laptop RAM & HDD")

# End User
print("Buying Lenovo Laptop")
lenovo = Lenovo() # TypeError: Can't instantiate abstract class Lenovo without an implementation for abstract method "ram_hdd"
lenovo.processor()
lenovo.ram_hdd()
lenovo.screen_saver()