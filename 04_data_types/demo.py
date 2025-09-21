# Data Types

# Numeric Types

# int
data = 10
print(type(data))

# float
data = 10.8
print(type(data))

# complex
data = 3 + 5j
print(type(data))

# string
data = "python"
print(type(data))

# boolean
data = True
print(type(data))

# List(homogenous data)
data = [10,20,30,40]
print(type(data))

# Tuple (heterogenous data)
data = (101,"Ravi",True)
print(type(data))

# Set
data = {1,2,3,4}
print(type(data))

# DIctionary 
data = {"name":"kiran", "id":101,"loaction":"hyd"}
print(type(data))

# None Type
x = None
print(type(x))

# User defined
class Student:
    #logics
    pass # syntax
student_john = Student()
print(type(student_john)) # <class '__main__.Student'> ---> __main__ indicates user defined datatype

# Type conversion
a = 10 # int
print(type(a))
b = 3.5 # float
print(type(b))
c = a + b # dynamic
print(c)
print(type(c))

# Type Casting
pi = 3.14 # float
print(type(pi))
print(pi)

# req round of pi and give whole number
pi_round_int = int(pi)
print(type(pi_round_int))
print(pi_round_int)

rating = "5"
print(type(rating))
# increment_rating = rating + 1 # TypeError: can only concatenate str (not "int") to str
increment_rating = int(rating) +1
print(increment_rating)
print(type(increment_rating))

new_rating = "four" # incompatible conversion
print(type(rating))
# increment_rating = int(new_rating) +1 # ValueError: invalid literal for int() with base 10: 'four'

num = 10
print(type(num))