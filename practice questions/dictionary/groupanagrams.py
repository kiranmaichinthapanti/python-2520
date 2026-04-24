words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result ={}

for word in words:
    key = "".join(sorted(word))

    if key in result:
        result[key].append(word)
    else:
        result[key] = [word]
        
print(list(result.values()))