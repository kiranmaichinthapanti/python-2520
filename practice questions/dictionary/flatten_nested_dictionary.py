d = {"a":1, "b": {"c":2,"d":3}}

# Output: {"a":1,"b.c":2, 'b.d':3}

result = {}

for k,v in d.items():
    if isinstance(v, dict):
        for sub_k, sub_v in v.items():
            result[k + "." + sub_k] = sub_v
    else:
        result[k] = v
        
print(result)