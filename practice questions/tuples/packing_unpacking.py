# Pack 3 values into a tuple
t = 10,20,30
print(t)

#Unpack a tuple into variables.
a,b,c = t
print(a)
print(b)
print(c)

# Swap two variables using tuples.
a1 = 10
b1 = 20

a1,b1 = b1, a1
print(a1,b1)

# Use * to capture remaining values.
t1 = (1,2,3,4,5)
num1,*num2,num3 = t1
print(num1)
print(num2)
print(num3)

# gnore values during unpacking
t2 = (10,20,30)
value1, _, value3 = t2
print(value1)
print(value3)

# Find maximum and minimum in tuple
print(max(t2))
print(min(t2))