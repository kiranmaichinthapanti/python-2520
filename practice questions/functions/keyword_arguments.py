# Call a function using keyword arguments instead of positional.
def sum(a,b):
    return a+b
print(sum(b=2,a=-4))

# Create a function student(name, marks) and call it using keywords.
def student(name,marks):
    print(f"My name is {name} and my marks is {marks}")

student(marks=90,name="kiranmai")

# Write a function to calculate simple interest:
# principal, rate, time → call using keyword arguments.

def simple_interest(principal,rate,time):
    return (principal*time*rate)/100

print(simple_interest(principal=20000,time=2,rate=4))    

# Mix positional and keyword arguments (valid & invalid cases).
def func(a,b,c):
    print(a,b,c)

func(1,2,c=3)
func(a=1,b=2,c=3)
func(1,2,3)
# func(a=1,2,3) SyntaxError: positional argument follows keyword argument

# What error occurs if you repeat the same argument twice?
def fun(a,b):
    print(a,b)

# fun(1,a=1) TypeError: fun() got multiple values for argument 'a'