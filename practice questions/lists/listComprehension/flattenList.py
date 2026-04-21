# Flatten nested list : converting nested list into single list with all elements

lst = [[1,2],[3,4],[5]]

# result = [num for sublist in lst for num in sublist]
# print(result)

result = []

for sublist in lst:
    for num in sublist:
        result.append(num)
print(result)

lst1 = [[1,2,3],[4,5,6]]

output = [num for sublist in lst1 for num in sublist if num%2==0]
print(output)