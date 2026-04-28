#  Write a function that takes another function and executes it.Pass a function as argument and call it inside.
def execute(func):
    func()

def greet():
    print("hello")

execute(greet)

# Create a function apply_operation(func, x, y).pass add/multiply functions
def apply_operation(func, x,y):
    return func(x,y)

def add(x,y):
    return x+y
def multiply(x,y):
    return x*y

print(apply_operation(add,2,3))
print(apply_operation(multiply,4,3))

# Use:map(), reduce(), filter() on a list
numbers = [1,2,3,4,7,8,9,10]
squares = list(map(lambda x:x*x, numbers))
print(squares)

even_numbers = list(filter(lambda n: n%2 == 0, numbers))
print(even_numbers)