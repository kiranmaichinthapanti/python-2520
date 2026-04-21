nums  = [1,2,3,4]
# nums.reverse()
# print(nums)

reverse = []

# for num in nums:
#     reverse.insert(0,num)
# print(reverse)

for num in nums[::-1]:
    reverse.append(num)
print(reverse)
