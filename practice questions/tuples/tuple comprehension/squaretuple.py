t = (1,2,3,4)

result = [num**2 for num in t]
print(tuple(result))

# Nested tuple modification challenge
t = ([1, 2], [3, 4])

t[0][0] = 100

print(t)