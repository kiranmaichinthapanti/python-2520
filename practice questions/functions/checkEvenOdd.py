def even_odd(num):
    if num%2==0:
        # print("Even")
        return "Even"
    else:
        # print("Odd")
        return "Odd"

result = even_odd(7)
print(result)

def odd_even(num):
    return "Even" if num%2 == 0 else "Odd"

res = odd_even(10)
print(res)


def check_numbers(nums):
    for num in nums:
        print(f"{num} is {"Even" if num%2==0 else "Odd"}")

check_numbers([1,2,3,4,7,8])

print("======Only even numbers======")
def check_only_even_numbers(nums):
   return [num for num in nums if num%2==0]

output=check_only_even_numbers([1,2,3,10,11,20])
print(output)

print("======Only odd numbers======")
def only_odd_numbers(nums):
    return [num for num in nums if num%2!=0]

response=only_odd_numbers([11,23,24,28,29,30])
print(response)

print("======Divisible by 2 and 3======")
def divisible_by_2_and_3(nums):
    for num in nums:
        if num%2 == 0 and num%3 == 0:
            print(f"{num} is divisible by 2 and 3")
    
divisible_by_2_and_3([1,2,20,30,3])

print("=======EVen or Odd taking input from user=====")
def check_even_or_odd(n):
    if n%2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

n = int(input("Enter a number: "))
check_even_or_odd(n)

print("=======Count even numbers========")
def count_even_numbers(nums):
    count = 0
    for num in nums:
        if num%2 == 0:
            count+=1
    return count

solution = count_even_numbers([1,2,3,4,7,8,9,10])
print("Even numbers count: ", solution)