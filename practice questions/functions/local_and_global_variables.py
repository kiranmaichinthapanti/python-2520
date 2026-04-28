# Create a global variable x = 10 and print it inside a function.
x = 10 # global variable
def global_variable():
    print("Accessing global variable inside function: ", x)

global_variable()

# Create a function with a local variable and try accessing it outside (observe error).
def local_variable():
    y = 10 # local variable
    print("Accessing local variable inside the function:",y)

local_variable()
# print("Accessing local variable outside the function: ", y) #NameError: name 'y' is not defined

# Write a function that adds a local and global variable
a = 10 # global variable
def add(b):
    return a+b

print("Adds a local and global variable a & b: ",add(2))

# Modify a global variable inside a function using global keyword.
ga = 20
def modify_ga():
    global ga
    ga = 40
    print("Modify ga value 20 to 40:", ga)

modify_ga()

# Write a function with a local variable having same name as global variable → observe output.
a = 10
def func(a):
    print(a)
func(20)

# Use globals() to access a global variable inside a function.
x = 40
def test():
    x = 20
    print(x)
    print(globals()['x'])

test()
print(x)

# Write a counter program using global variable.
count = 0
def counter():
    # count += 1 #UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    global count
    count += 1
    print(count)
counter()

# Rewrite the counter program without using global (important).
def counter1():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    return increment
c= counter1()
print(c())