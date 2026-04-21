list1 = [1,2,3]
list2 = [3,4,5]

result = []

for num in list1 + list2:
    if num not in result:
        result.append(num)
print(result)