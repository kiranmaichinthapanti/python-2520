# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
def singleNumber(nums):
    result = []
    for num in nums:
        if nums.count(num) == 1:
            result.append(num)
    return result
        
print(singleNumber([1,2,3,4,2,3,4]))
print(singleNumber([1,1,2,3,4,2,3,4,8,9]))

