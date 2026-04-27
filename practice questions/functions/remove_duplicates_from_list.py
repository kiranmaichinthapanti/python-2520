def remove_duplicates(nums):
    result= []
    for num in nums:
        if num not in result:
            result.append(num)
    return result

print(remove_duplicates([1,2,2,3,4,7,8,8]))