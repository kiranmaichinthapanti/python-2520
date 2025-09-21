# Operators

# Arithmetic Operators
num1 = 3
num2 = 2
print(f"Sum of {num1} and {num2} is {num1+num2}")
print(f"Difference of {num1} and {num2} is {num1-num2}")
print(f"Product of {num1} and {num2} is {num1*num2}")
print(f"Division of {num1} and {num2} is {num1/num2}")
print(f"Modulus of {num1} and {num2} is {num1%num2}")

print(num1//num2)
print(num1**num2) # 3 ^ 2

# Compound Assignment Operators
num = 10
num = num + 5 # without Compound Assignment Operators
print(num)

num = 10
num+=5 
print(num) # with Compound Assignment Operators
num*=5 
print(num)

count = 1
# increment count
count += 1
print(count)

count = 10
# increment count
count -= 1
print(count)

# Comparison Operators
a = 10
b = 5
c = 3
d = 2

print(a == b)
print(a > b)
print(a < b)
print(a != b)
print(a >= b)
print(a <= b)

# Logical Operators
res_and = a > b and c < d # T and F ==> F
print(res_and)
res_and = a > b and c > d # T and T ==> T
print(res_and)

res_or = a > b or c < d # T and F ==> T
print(res_or)

res_or = a > b # T
print(not res_or) # F

# Memebership Operators
# string is a sequence data type
data = "python"
is_z_present = "z" in data
print(is_z_present)
is_p_present = "p" in data
print(is_p_present)

is_python_present = "python" in data
print(is_python_present)

# employees
emp_id = 111
emp_ids = [101,102,103,104,105,106,107,108,109,110]
is_id_present = emp_id in emp_ids
print(is_id_present)

is_id_not_present = emp_id not in emp_ids
print(is_id_not_present)

# Identity Operators
a= 10
b = 10
print(a == b) # comparison of values
print(a is b) # comparison of memory
print(id(a))
print(id(b))

a = [10,20]
b = [10,20]

print(a == b) # comparison of values
print(a is b) # comparison of memory
print(id(a))
print(id(b))

# Bitwise Operators

num1 = 5 # 0000000000000101
num2 = 3 # 0000000000000011
         # 0000000000000001 (&)
         # 0000000000000111 (|)
print(num1 & num2)
print(num1 | num2)
