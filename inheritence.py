'''
Created on Jan 21, 2018

@author: kripa
'''
"""class A:
    name  = "rohit"
    def __init__(self):
        print("this is class A.")
    def m_a(self):
        print("this method is from A class.")

class B(A):
    age = 40
    def __init__(self):
        A.__init__(self)
        print("this is class B.")
    def m_b(self):
        print("this method is from class B.")
        
class C(B):
    address = "blr"
    def __init__(self):
        B.__init__(self)
        print("this is class C.")
    def m_c(self):
        print("this imethod is from c class")

class D:
    def __init__(self):
        print("this is class D.")


obj_C = C()
print(obj_C.name)
print(obj_C.age)
print(obj_C.address)

obj_A = A()
obj_B = B()
print(obj_B.name)
obj_B.m_a()
print(obj_B.age)
obj_B.m_b()
print(dir(obj_B))
"""
"""class A:
    name  = "rohit"
    def __init__(self):
        print("this is class A.")
    def m_a(self):
        print("this method is from A class.")
    def print_msg(self):
        print("print using class A.")

class B:
    age = 40
    def __init__(self):
        print("this is class B.")
    def m_b(self):
        print("this method is from class B.")
    def print_msg(self):
        print("print using class B")    
        
class C:
    address = "blr"
    def __init__(self):
        print("this is class C.")
    def m_c(self):
        print("this imethod is from c class")
    def print_msg(self):
        print("using class C.")    
class D(C,A,B):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        A.__init__(self)
        print("this is class D.")

obj_D = D()
obj_D.print_msg()
"""
"""class Fruit:
    def cost(self,fruit_name="orange",cost = None):
        print("print cost of fruits.")
        print("Fruit name is {}".format(fruit_name))
        if cost == None:
            print("this fruit is free of cost.")


ins = Fruit()
ins.cost('Apple')
ins.cost()
ins.cost('mango',90)
"""


class A:
    count = 0
    def __init__(self):
        A.count +=1
    def __del__(self):
        A.count -=1    
        
obj = A()
print(A.count)
obj1 = A()
print(A.count)
obj2 = A()
print(A.count)
obj3 = A()
print(A.count)
obj4 = A()
print(A.count)
del obj3
print(A.count)
del obj2
print(A.count)





















