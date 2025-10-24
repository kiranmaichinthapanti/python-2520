# Encapsulation

class A:
    def __init__(self,a,b):
        self._a = a # protected
        self._b = b # protected

class B(A):
    def showA(self):
       a = A(20,30)
       print(a._b)

obj = B(10,20)
obj.showA()