nums = [1, 5, 7, -1, 5]
target = 6
# Output: 3 pairs
count = 0

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            # print(nums[i],nums[j])
            count += 1
print(count)