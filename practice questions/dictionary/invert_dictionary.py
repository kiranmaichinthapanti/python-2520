d = {"a":1, "b": 2}
# output : {1:'a',2:'b'}

result  = {}

for k,v in d.items():
    result[v] = k
print(result)