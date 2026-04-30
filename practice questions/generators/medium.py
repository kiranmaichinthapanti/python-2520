# Create a generator that yields squares of numbersCreate a generator that yields squares of numbers
def square_numbers():
    for i in range(1,11):
        yield i*i
result = square_numbers()
for r in result:
    print(r)
# [0R]
squares = (i*i for i in range(1,11))
for s in squares:
    print(s)

#  Create a generator for Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a,b = b, a+b

for num in fibonacci(6):
    print(num)

