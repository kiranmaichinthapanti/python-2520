nums = [1, -2, 3, -4, 5]

result = [0 for num in nums if num <0]
print(result)

output = [0 if num < 0 else num for num in nums]
print(output)