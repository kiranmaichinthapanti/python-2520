# without function

a = 10
b = 5

# math operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 20
b = 10

# math operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 200
b = 100

# math operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("========================")

# with function
def maths_ops():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# call function with 20 & 10
a = 20
b = 10
maths_ops()
a = 10
b = 5
maths_ops()
a = 200
b = 100
maths_ops()

print("==================")

# with function using parameters
def maths_ops(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# maths_ops() # TypeError: maths_ops() missing 2 required positional arguments: 'a' and 'b'
maths_ops(20,10)
maths_ops(200,100)
maths_ops(10,5)

# a,b are parameters
# (200,100) are arguments
print("====================")

# Positional Arguments
def login(username,password):
    if username == "kiran" and password == "1234":
        print("Login Success")
    else:
        print("Login Failed")

login("1234","kiran") # order messed up
login("kiran","1234") # order is correct
# login() # TypeError: login() missing 2 required positional arguments: 'username' and 'password'
# login("ravi") # TypeError: login() missing 1 required positional argument: 'password'

# employee info function
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")

employee_info("hyderabd","ravi","ravi@gmail.com")
employee_info("kiran","kiran@gmail.com","hyderabad")
# employee_info("krishna","pune") # TypeError: employee_info() missing 1 required positional argument: 'emp_location'

# Keyword Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")

employee_info("hyderabd","ravi","ravi@gmail.com")
# passsed explicitly by specifying the name
employee_info(emp_location="hyderabad",emp_name="kiranmai",emp_email="kiran@gmail.com") # keyword
print("==============================")

# Default Arguments
def employee_info(emp_name,emp_email,emp_location,company_name="Google"):
    print(f"Hi {emp_name}, your email is {emp_email} working for {company_name} and work location is {emp_location}")

employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com")
employee_info(emp_location="pune",emp_name="john",emp_email="john@gmail.com")
employee_info(emp_location="bangalore",emp_name="krishna",emp_email="krishna@gmail.com")
employee_info(emp_location="bangalore",emp_name="krishna",emp_email="krishna@gmail.com",company_name="META")

# Arbitrary Positional Arguments(*args)
def add_all(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    print(f"The Total Sum is {total}")

add_all(10)
add_all(10,20)
add_all(10,20,30,40,70)

# Arbitrary Keyword Arguments(**kwargs)
def profile(**info):
    print(info)

profile(name="kiran")
profile(name="kiran", location="hyd")
profile(name="kiran", location="hyd", age = 20)

def credit_trans(**trans):
    print(trans)
    toatl = 0
    for tran in trans:
        print(tran)
credit_trans(jan=1000,feb=2000,mar=3000)

# NOTE : just like dict it's considering only keys

# To get value => we need key
def credit_trans(**trans):
    print(trans)
    toatl = 0
    for tran in trans:
        print(trans[tran])
credit_trans(jan=1000,feb=2000,mar=3000)

# using both to do some calculations
def credit_trans(**trans):
    print(trans)
    toatl = 0
    for tran in trans:
        total = toatl + trans[tran]
    print(f"You have done {len(trans)} which amounts to total of {total}")
credit_trans(jan=1000,feb=2000,mar=3000)

# without return keyword
def add(a,b):
    a+b

add(10,20)
print(add(10,20))

# with return keyword
def add(a,b):
   return a+b

add(10,20)
print(add(10,20))

def add(a,b):
    return a+b
    print("See if this will be printed")

print(add(10,20))

def math_ops(a,b):
    return a+b
    return a-b
    return a/b

print(math_ops(100,200))

def math_ops(a,b,opr):
    if opr == "+":
        return a+b
    elif opr == "*":
        return a*b
    elif opr == "/":
        return a/b
    else:
        return "Invalid Operator Selected"
    
print(math_ops(100,200,"*"))
print(math_ops(100,200,"/"))
print(math_ops(100,200,"+"))
print(math_ops(100,200,"-"))

# Function Composition
def add(a,b):
    return a+b

def sub(c,d,e):
    return add(c,d) - e

print(sub(3,4,5)) # add c & d from that minus - e # 2

# local scope
def add():
    # local variable
    la = 10
    lb = 5
    print(la) # access local variable within function
    print(lb) # access local variable within function

add()

# trying to access local variable outside function
# print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?

# local scope
def add(la,lb):
    print(la) # access local variable within function
    print(lb) # access local variable within function

add(30,40)

# trying to access local variable outside function
# print(la)

# global variable
ga = 30

def add(la,lb):
    print(la) # access local variable within the function
    print(lb) # access local variable within the function
    print(ga) # access global variable within the function
add(10,20)

print(ga) # access global variable outside function

# name conflict
ga = 30

def add(la,lb, ga):
    print(la) # access local variable within the function
    print(lb) # access local variable within the function
    print(ga) # access local variable within the function
    print(globals()['ga']) # access global varibale ga within the function
    print(la+lb+ga)

add(1,2,3)

# trying to change global variable
count = 0
count += 1
print(count)

count = 0
def increment():
    global count
    count += 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value

increment()
print(count)

# Function Types in Python

# get predefined functions
import builtins
print(dir(builtins))

# without Lambda
def add(a,b):
    return a+b
print(add(3,4))

# with lambda
# lambda arguments: expression
sum = lambda a,b: a+b
print(sum(10,20))

# IILE
print((lambda a,b:a+b)(5,8))

# without lambda
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
print(is_even(5))
print(is_even(10))

# with lambda
even = lambda num : True if num % 2 == 0 else False
print(even(10))

print((lambda num:num % 2 == 0)(5))
print((lambda num:num % 2 == 0)(4))

print((lambda num:num % 2 != 0)(4))
print((lambda num:num % 2 != 0)(5))


print((lambda num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero")(10))
print((lambda num: "Positive" if num > 0 else "Negative")(10))


employee_info = lambda emp_name,emp_email,emp_location: print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")
employee_info("ravi","ravi@gmail","hyd")

# regular function
def greet(name):
    print("Hello",name)
    print("Welcome To Python")

greet("ravi")

def add_nums(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add_nums(1,2,3))

# without map()
# write a script to take a list of numbers and return square of list of number
# [1,2,3,4,5] => [1,4,9,16,25]

def square_list(numbers):
    square_list = []
    for num in numbers:
        square_list.append(num*num)
    return square_list

print(square_list([1,2,3,4,5]))

# with map()
# write a script to take a list of numbers and return square of list of number
# [1,2,3,4,5] => [1,4,9,16,25]
# map(function, iterable)
print(list(map(lambda num: num * num, [1,2,3,4,5]))) # <map object at 0x00000275264D2F80>

# without filter()
# write a script to take a list of numbers and return only even numbers from the list
# [1,2,3,4,5,6,7,8,9,10] => [2,4,6,8,10]
def even_list(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

print(even_list([1,2,3,4,5,6,7,8,9,10]))

# with filter()
# write a script to take a list of numbers and return only even numbers from the list
# [1,2,3,4,5,6,7,8,9,10] => [2,4,6,8,10]
print(list(filter(lambda num: num % 2 == 0, [1,2,3,4,5,6,7,8,9,10]))) # <filter object at 0x0000021B46FD3520>

# without reduce()
# write a script to take a list of numbers and return product of all the items in the list
# [1,2,3,4,5] => 1*2*3*4*5 = 120
def multiply_list(numbers):
    result = 1
    for num in numbers:
       result = result * num
    return result

print(multiply_list([1,2,3,4,5]))

# with reduce()
# write a script to take a list of numbers and return product of all the items in the list
# [1,2,3,4,5] => 1*2*3*4*5 = 120
# import reduce
from functools import reduce
print(reduce(lambda result,num: result * num, [1,2,3,4,5]))

data = [100,None,80,70,None]
filter_data = (list(filter(lambda num: num is not None, data)))
print(filter_data)

servers = ["10.0.0.1","down","10.0.0.3","10.0.0.3","down"]
active_servers = list(filter(lambda server: server !="down", servers))
print(active_servers)