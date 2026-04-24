d = {"a": 3, "b": 1, "c": 2}

result = {}

for k in sorted(d,key=d.get):
    result[k] = d[k]
print(result)