# Create a generator that yields numbers from 1 to 10
def numbers():
    for i in range(1,11):
        yield i
result = numbers()
for r in result:
    print(r)

# Create a generator for even numbers
def even_numbers():
    for i in range(1,11):
        if i%2 == 0:
            yield i
result = even_numbers()
for num in result:
    print(num)