t = (10, 20, 4, 45, 99)

# float('-inf') means negative infinity — a value smaller than any number.
largest = second = float('-inf')

for num in t:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(second)
