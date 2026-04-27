# Write a function that prints all key-value pairs.
def print_all_key_value(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_all_key_value(name = "kiran", age = 27)

# Pass name, age, city and print them.
print_all_key_value(name = "kiran", age = 27, city="Hyderabad")

# Write a function to find the highest value in **kwargs.
def highest_value(**kwargs):
    values = list(kwargs.values())
    max_value = values[0]

    for value in values:
        if value > max_value:
            max_value = value
    return max_value

print("Highest value: ", highest_value(a=20,b=30,c=40))

# Create a function to count number of keys passed.
def num_of_keys(**kwargs):
    count = 0
    for key in kwargs:
        count += 1
    return count

print("number of keys passed: ", num_of_keys(name="kiran", age = 27))

# Write a function that:
# prints only keys where value > 50

def func(**kwargs):
    for key,value in kwargs.items():
        if value > 50:
            return key
print("print keys values above 50: ",func(a=80,b=40,c=10))

# Convert **kwargs into a dictionary and sort it.
def convert_kwargs_dictionary(**kwargs):
    return dict(sorted(kwargs.items()))

print(convert_kwargs_dictionary(name="kiran",age=27))

# Write a function using: positional default *args together
def calculate_total(price,tax=5,*args):
    total = price + tax

    # add extra charges from *args
    for extra in args:
        total += extra
    
    return total

print(calculate_total(100))
print(calculate_total(100,10))
print(calculate_total(100,10,20,30))

# Write a function using: *args and **kwargs
def display_data(*args, **kwargs):
    print("Positional arguments: ")
    for arg in args:
        print(arg)

    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(key, ":", value)

display_data(1,2,3, name="kiran", age=27)