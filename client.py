# Client needs custom math package

from math_package import add,mul,sub
print("Value Of Var: ",add.var)
print("Sum Of Nums: ",add.add_fun(10,5))
print("Product Of Nums: ",mul.mul_fun(10,5))
print("Diff Of Nums: ",sub.sub_fun(10,5))
print("="*50)

import math_package.add
import math_package.sub
import math_package.mul

print("Value Of Var: ",math_package.add.var)
print("Sum Of Nums: ",math_package.add.add_fun(10,5))
print("Product Of Nums: ",math_package.mul.mul_fun(10,5))
print("Diff Of Nums: ",math_package.sub.sub_fun(10,5))
