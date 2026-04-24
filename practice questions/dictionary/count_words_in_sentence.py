s = "python is easy python is powerful"
freq = {}

for word in s.split():
    if word in freq:
        freq[word] +=1
    else:
        freq[word] = 1
print(freq)