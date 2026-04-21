s = "hello world"

vowels = "aeiouAEIOU"

count = 0

for char in s:
    if char in vowels:
        count +=1
print(count)

vowels = [ch for ch in s.lower() if ch in vowels]
print("no of vowels", len(vowels))