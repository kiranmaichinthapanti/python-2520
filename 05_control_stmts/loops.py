# Loops: repetitive actions
counter = 1

while counter <= 5:
    print(counter)
    counter = counter+1

# used when you don't know number of iterations in advance
atm_pin = 7689 # actual pin
user_input = 0

while user_input != atm_pin:
    user_input = int(input("Enter pin: "))

print("You can withdraw")

# for loop

# used to iterate over a sequence
data = 10 # int : not a sequence
print(id(data)) # memory address
print(type(data)) # data type
print(dir(data)) # attributes supported

# for character in data: # TypeError: 'int' object is not iterable
#     print(character)

data = "ten" # string
print(type(data))
print(dir(data))

for character in data:
    print(character)

# how to know iterable object - dir(object)

list_numbers = [10,20,30,40,50] # [ ] - list
list_numbers = [10]
print(type(list_numbers))
print(dir(list_numbers))
for number in list_numbers:
    print(number)

# used when you know number of Iterations in advance
for times in range(11):
    print("Good Morning")

# range(start,stop,step)
for num in range(5,10): # 5,6,7,8,9
    print(num)

for num in range(2,11,1): 
    print(num)

for num in range(2,11,2): 
    print(num)

for num in range(5,100,5): 
    print(num)

for num in range(10,0,-1): 
    print(num)