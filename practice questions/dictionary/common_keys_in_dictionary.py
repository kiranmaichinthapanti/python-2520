d1 = {"a":1,"b":2}
d2 = {"b":3,"c":4}

result = {}

for k in d1:
    if k in d2:
        result[k] = d1[k]
print(result)