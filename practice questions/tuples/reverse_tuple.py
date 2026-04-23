t = (1, 2, 3, 4)

result = []
for num in t:
    result.insert(0,num)

result = tuple(result)

print(result)


output = t[::-1]
print(output)