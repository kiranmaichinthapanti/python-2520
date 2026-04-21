nums = [1,2,2,3,3,4]


# for num in nums:
#     if num not in result:
#         result.append(num)
# print(result)

result =[] 
[result.append(num) for num in nums if num not in result]

print(result)