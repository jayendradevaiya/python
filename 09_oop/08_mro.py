class A:
    lable = "A: Base class"

class B(A):
    lable = "B: Masala blend"

class C(A):
    lable = "C: herbal blend"

class D(C,B):
    pass

cup = D()
print(cup.lable)
print(D.__mro__)

"""This is used for findinig which flow of inheritance has come """