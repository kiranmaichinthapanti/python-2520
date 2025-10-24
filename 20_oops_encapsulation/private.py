# Encapsulation

class A:
    def __init__(self,a,b):
        self.__a = a # private
        self.__b = b # private

obj = A(10,20)

# print(obj.a) # accessible
# print(obj.b) # accessible

# print(obj._Myclass_private_variable)
print(obj._A__a) # accessing via name mangling