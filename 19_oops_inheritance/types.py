# Types Of Inheritance

# Single Level Inheritance : One Parent -> One Child

class Father:
    def house(self):
        print("Has House")

class Son(Father):
    def car(self):
        print("Has Car")

son_obj = Son()
son_obj.car()
son_obj.house()

# Multi Level Inheritance: Parent -> Child -> GrandChild
class GrandParent:
    def land(self):
        print("Has Agricultural Land")

class Father(GrandParent):
    def house(self):
        print("Has House")

class Son(Father):
    def car(self):
        print("Has Car")

son_obj = Son()
son_obj.car()
son_obj.house()
son_obj.land()

# Multiple Inheritance : One Child -> Multiple Parents
class Father:
    def house(self):
        print("Has House")
    
class Mother:
    def gold(self):
        print("Has Gold")

class Son(Father,Mother): # applying mutiple inheritance
    def car(self):
        print("Has Car")

son_obj = Son()
son_obj.car()
son_obj.house()
son_obj.gold()

# Hierarchical Inheritance : One Parent -> Multiple Child
class Father:
    def house(self):
        print("Has House")
        
class Daughter(Father):
    def business(self):
        print("Has Business")

class Son(Father): 
    def car(self):
        print("Has Car")

son_obj = Son()
son_obj.car()
son_obj.house()

daughter_obj = Daughter()
daughter_obj.business()
daughter_obj.house()

# Hybrid Inheritance : Combination of two or more types
class A:
    def feature1(self):
        print("Feature 1")

class B(A):
    def feature2(self):
        print("Feature 2")

class C(A):
    def feature3(self):
       print("Feature 3")

class D(B,C):
    def feature4(self):
        print("Feature 4")

d_obj = D()
d_obj.feature4()
d_obj.feature3()
d_obj.feature2()
d_obj.feature1()