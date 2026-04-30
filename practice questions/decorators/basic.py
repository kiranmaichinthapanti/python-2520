# create a decorator that prints "start" and "end"
def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator
def greet(name):
    print("Hello", name)

greet("Abhilash")

# Decorate a function that prints your name
def prints_name(func):
    def wrapper(*args,**kwargs):
        print("Printing name...")
        result = func(*args,**kwargs)
        print("Done printing name")
        return result
    return wrapper

@prints_name
def greet_name(name):
    print("Hello",name)

greet_name("Kiranmai")