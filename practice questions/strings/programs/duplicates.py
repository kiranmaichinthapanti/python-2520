s = "programming"

unique = ""

for char in s:
    if char not in unique:
        unique += char
print(unique)