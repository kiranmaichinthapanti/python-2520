# Create a decorator to check if number is positive
def check_number_positive(func):
    def wrapper(num):
        if num > 0:
            print("Number is positive, proceeding....")
            return func(num)
        else:
            print("Number is not positive, blocked!")
    return wrapper

@check_number_positive
def positive(num):
    print(f"{num} is a valid positive number")

positive(-10)
positive(4)

# Create logging decorator (print function name)
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args,**kwargs)
        print(f"Finished executing: {func.__name__}")
        return result
    return wrapper

@log_function
def greet(name,age =24):
    print("Hello",name,age)

@log_function
def add(a,b):
    return a + b

# Function calls
greet("Kiranmai", age=27)

result = add(10,20)
print("Result: ", result)