""" 
If two or more classes that are inherited in a new class has both same attributes or methods.
With MRO we can know which one will have more priority. 
"""

class A:
    def hablar(self):
        print("Sonido, sonido desde A")

class F(A):
    def hablar(self):
        print("Sonido, sonido desde F")

class B(F, A):
    pass

class C(F):
    def hablar(self):
        print("Sonido, sonido desde C")

class D(B, C):
    pass

d = D()

#d.hablar()
print(D.mro())
F.hablar(d)
C.hablar(d)