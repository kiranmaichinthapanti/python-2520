nums = [1,1,2,2,2,3]

freq = {}
for num in nums:
    if num in freq:
        freq[num].append(num)
    else:
        freq[num] = [num]
print(freq)
