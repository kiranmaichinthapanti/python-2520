# Write a function to sum all numbers using *args.
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1,2,3))


def total(*args):
    total_sum = 0
    for num in args:
        total_sum += num
    return total_sum
print(total(4,8,9,10))

# Write a function to print all arguments.
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1,2,3,"Hello", True)

# Write a function to find the maximum number using *args.
print("======maximum numbers using *args=====")
def max_number(*args):
    max_value = args[0]
    for num in args:
        if num > max_value :
            max_value = num
    return max_value

print(max_number(10,80,20))

# Write a function to multiply all numbers.
print("=====multiply all numbers======")
def multiply_numbers(*args):
    mul = 1
    for num in args:
        mul *= num
    return mul
print("Multiply of all numbers : ", multiply_numbers(2,3,9))

# Write a function that returns:
# sum of even numbers
# sum of odd numbers
# from *args
def even_sum_and_odd_sum(*args):
    even_sum = 0
    odd_sum = 0
    for num in args:
        if num%2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return {
        "even_sum" : even_sum,
        "odd_sum" : odd_sum,
        "count" : len(args) 
    }

print("Even sum and ODD sum is : ", even_sum_and_odd_sum(1,2,3,4,5,6,7,8,9,10))

def odd_sum_and_even_sum(*args):
    even_sum = sum(num for num in args if num%2 == 0)
    odd_sum = sum(num for num in args if num%2 != 0)
    return even_sum, odd_sum

print('odd sum and even sum : ', odd_sum_and_even_sum(1,2,3,4,5,6,7,8,9,10))

# Write a function that filters only positive numbers.
def positive_numbers(*args):
    positive_num = []
    for num in args:
        if num > 0:
            positive_num.append(num)
    return positive_num
print("Positive Numbers: ", positive_numbers(-10,10,89,-20,3,4))