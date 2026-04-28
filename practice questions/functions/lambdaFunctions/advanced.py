# Write a lambda to find maximum of two numbers.

max_number = lambda a,b: a if a>b else b
print(max_number(10,2))

# Use lambda inside another function.
def multiply(n):
    return lambda x: x*n

double = multiply(2)
print(double(4))
triple = multiply(3)
print(triple(3))

# Create a lambda that returns another lambda.
add = lambda a: (lambda b: a + b)
result = add(3)(4)
print(result)

# reverse string
reverse_string = lambda s: s[::-1]
print(reverse_string("kiran"))