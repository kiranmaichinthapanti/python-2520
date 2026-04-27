# Write a function that takes two numbers and returns their sum.
def sum(a,b):
    return a+b

print(sum(2,3))

#  Write a function that takes name and age and prints:
# "My name is ___ and I am ___ years old"

def func(name,age):
    print(f"My name is {name} and I am {age} years old")

func("Kiran",24)

# Write a function to find the maximum of 3 numbers using positional arguments.
def max_numbers(n1,n2,n3):
    max_value = n1
    if n2 > max_value:
        max_value = n2
    if n3 > max_value:
        max_value = n3
    return max_value

print(max_numbers(2,3,4))

# Write a function that takes a string and a character, and counts how many times the character appears.
def counts_character(str,ch):
    count = 0
    for c in str:
        if c == ch:
            count += 1
    return count

print(counts_character("kiranmai",'a'))

# Write a function that takes 3 numbers and returns the second largest.
def second_largest(num1,num2,num3):
    if (num1>=num2 and num1<=num3) or (num1<=num2 and num1>=num3):
        return num1
    elif (num2>=num1 and num2<=num3) or (num2<=num1 and num2>=num3):
        return num2
    else:
        return num3
print(second_largest(10, 25, 15))
