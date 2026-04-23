t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
# Output: (3, 4)

result = []

for num in t1:
    if num in t2:
        result.append(num)

result = tuple(result)

print(result)