nums = [1,2,2,3,4,7,7,3,3]

freq={}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)