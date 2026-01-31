class A:
    def method_a(self):
        print("A")
class B(A):
    def method_b(Self):
        print("B")
class C(A):
    def method_c(self):
        print("C")
class D(B,C):
    def method_d(self):
        print("D")
d=D()
d.method_a()
d.method_b()
d.method_c()
d.method_d()
