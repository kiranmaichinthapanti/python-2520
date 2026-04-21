text = "Python is very easy"

words = text.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)