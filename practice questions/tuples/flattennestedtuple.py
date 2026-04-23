t = (1, (2, 3), (4, 5))

result = []

for subset in t:
    if isinstance(subset, tuple):
        for num in subset:
            result.append(num)
    else:
        result.append(subset)

result = tuple(result)
print(result)
        
