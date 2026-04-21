nums=[1,2,2,3,3,4]

result = []

for num in nums:
    if num not in result:
        result.append(num)
print(result)