def max_of_3_numbers(nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value

print(max_of_3_numbers([20,20,40]))
print(max_of_3_numbers([20,0,-40]))
