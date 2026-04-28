# Use lambda with filter() to get even numbers from list.
even_numbers = filter(lambda n: n%2 == 0, [20,21,9,30,1,7,40])
print(list(even_numbers))