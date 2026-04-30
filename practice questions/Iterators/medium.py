# Create custom iterator for even numbers
nums = [1,2,3,4,5,6,7,8,9,10]
num_iter = iter(nums)
while True:
    try:
        num = next(num_iter)
        if num%2 == 0:
            print(num)
    except StopIteration:
        break

# Create iterator that prints numbers in reverse
n1 = [20,90,10,80,77,22,13]
rev_iter = iter(reversed(n1))
while True:
    try:
        print(next(rev_iter))
    except StopIteration:
        break