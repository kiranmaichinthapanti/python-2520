# Create a dictionary with 3 key-value pairs
d = dict(name="kiran", age = 27, salary= 30000)
print("Initial dictionary:", d)

# Access a value using a key.
print("Access name: ", d['name'])

# Add a new key-value pair.
d['location'] = 'hyd'
print("After adding location:", d)

# Update an existing value
d['name'] = 'puppy'
print("After updating name:",d)

# delete a key from dictionary
d.pop("location")
print("After deleting location:", d)