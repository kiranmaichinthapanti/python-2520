d = {"a": 1, "b": 2, "c": 1}

result = {}

for k,v in d.items():
    if v not in result.values():
        result[k] = v
print(result)