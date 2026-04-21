nums = [1, 2, 3, 2, 4, 2]
val = 2

result = []

for num in nums:
    if num != val:
        result.append(num)
print(result)