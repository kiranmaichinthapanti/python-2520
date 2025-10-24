# Abstraction

# Laptop Manufacturer

# Laptop Contract / Interface (govt said these are must for laptop)

# Without Abstraction

# Concrete Class
class Laptop:

    # Concrete Methods
    def processor(self):
        print("Laptop Processor ")

    def ram_hdd(self):
        print("Laptop RAM & HDD")

# Implementation
class Lenovo(Laptop):

    def processor(self):
        print("Lenovo Laptop Processor ")

class Dell(Laptop):

    def ram_hdd(self):
        print("Dell Laptop RAM & HDD")

# End User
print("Buying Lenovo Laptop")
lenovo = Lenovo()
lenovo.processor()

print("Buying Dell Laptop")
dell = Dell()
dell.ram_hdd()

laptop = Laptop()
laptop.processor()
laptop.ram_hdd()