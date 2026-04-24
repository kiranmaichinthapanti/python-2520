s = "programming"
# Output: {'p':1, 'r':2, 'o':1, 'g':2, 'a':1, 'm':2, 'i':1, 'n':1}

freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0) + 1
 
max_char = None
max_count = 0

for ch in freq:
    if freq[ch] > max_count:
        max_count = freq[ch]
        max_char = ch

print("Most frequent character in string: ", max_char)
print("Frequency: ", max_count)