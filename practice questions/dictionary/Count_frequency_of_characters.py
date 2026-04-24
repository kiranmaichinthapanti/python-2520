s = "aabbccdde"
# Output: {'a':2, 'b':2, 'c':2, 'd':2}

freq = {}

for ch in s:
    freq[ch] = freq.get(ch,0) + 1
print(freq)