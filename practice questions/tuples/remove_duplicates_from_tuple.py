t = (1, 2, 2, 3, 4, 4)

result = []

for num in t:
    if num not in result:
        result.append(num)
result = tuple(result)
print(result)