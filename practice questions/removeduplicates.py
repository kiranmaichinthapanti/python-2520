# Remove Duplicates from list

nums = [1,2,3,4,1,2,7,8,9,8,9]
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)
print(unique)

# use list comprehension
nums = [1,1,2,2,3,3,4,4,8,8,9]
unique = []
[unique.append(num) for num in nums if num not in unique]
print(unique)

# use lambda
nums = [1,1,2,2,3,3,4,4,8,8,9]
unique = []
list(filter(lambda n: not(n in unique or unique.append(n)), nums))
print(unique)
