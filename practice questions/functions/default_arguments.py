# Write a function greet(name="Guest") and test both cases.
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("kiran")
greet(name="abhii")

# Create a function to calculate square with default value 2.
def square(value = 2):
    return value*value

print(square(4))
print(square())

# Write a function to calculate power:
# base, exponent=2
def power(base,exponent=2):
    return base**exponent

print(power(3))
print(power(2,3))

# Write a function that calculates salary with default bonus = 1000.
def calculate_salary(base_sal,bonus=1000):
    return base_sal + bonus

print(calculate_salary(20000))
print(calculate_salary(30000,2000))

# What happens if default argument comes before non-default? Try and fix.
# # def f(a=10,b): # SyntaxError: parameter without a default follows parameter with a default
#     print(a,b)
# f(3)  

def f(a,b=10):
    print(a,b)
f(3)

# Create a function with multiple default arguments and test combinations.
def student(name="Guest", marks=0, grade="N/A"):
    print(f"Name: {name}, Marks: {marks}, Grade: {grade}")

student()
student("ABhii")