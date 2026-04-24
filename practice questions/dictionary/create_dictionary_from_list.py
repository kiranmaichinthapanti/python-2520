keys = ["a", "b", "c"]
values = [1, 2, 3]
# Output: {'a':1, 'b':2, 'c':3}

result = dict(zip(keys,values))

print(result)

# Unzip dictionary
a,b = zip(*result.items())
print(a)
print(b)