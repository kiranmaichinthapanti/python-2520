# Create a tuple with 5 elements and print it
t1 = (1,2,3,4,5)
print("Tuple",t1)

# create a single element tuple correctly
t2 = (2,)
print("Single element tuple",t2)

# Access the 3rd element of a tuple
print("access 3rd element",t1[2])

# Slice a tuple to get first 3 elements
print("First 3 elements",t1[0:3])

# . Check if an element exists in a tuple
if 3 in t1:
    print("Element exists")
else:
    print("Element not found")