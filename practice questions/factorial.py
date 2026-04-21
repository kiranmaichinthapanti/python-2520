def fact(num):
    return 1 if num == 0 else num*fact(num-1)

print(fact(5))

num = int(input("Enter the number"))
fact = 1
for i in range(1,num+1):
    fact *= i

print(f"factorial of {num} is {fact}")
