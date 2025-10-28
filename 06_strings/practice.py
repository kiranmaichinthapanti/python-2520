print("mango" and "apple")

class A:
    def test1(self):
        print("method named test1 of A called")
    
class B(A):
    def test1(self):
        print("method named test1 of B called")

class C(A):
    def test1(self):
        print("method named test1 of C called")

class D(B,A):
    def test2(self):
        print("method named test1 of D called")

obj = D()
obj.test1()

print("afzal",end="@")
print("CodingNinjas")