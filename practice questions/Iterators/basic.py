# Convert a list into iterator and print elements using next()
l1 = [1,2,3,4,8]
it = iter(l1)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# Create an iterator for a string
name = "Kiranmai"
name_iter = iter(name)
while True:
    try:
        print(next(name_iter))
    except StopIteration:
        break