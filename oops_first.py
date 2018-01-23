'''
Created on Jan 17, 2018

@author: kripa
'''
'''
class A:
    pass

print(type(A))
print(id(A))
obj = A()
print(obj)
print(id(obj))

obj1 = A()
print(id(obj1))

obj3 = A()
print(id(obj3))

var = 50
print(id(var))
'''
'''
from sys import getsizeof

class Employee:
    pass

e1 = Employee()
print(e1)
e1.name = "rohit"
e1.address = "blr"
e1.age = 90
e1.temp = "hghggxsgcgxghcbkiagcgdusafuasgkcukgchjxbcfjfsfghsgbfashfgjgfbhzbhjcjdbhdbihfkfgk"
print(getsizeof(e1.temp))
print(e1.name)
print(getsizeof(e1))
e2 = Employee()
print(e2)
e2.name = "rohan"
e2.address = "delhi"
e2.age = 45
print(e2.age)
print(getsizeof(e2))

e3 =Employee()
e4 = Employee()
print(e3)
print(e4)
e5 = e4
print(e5)
e4.name = "e4"
print(e4.name)
print(e5.name)
e5.name = "e5"
print(e4.name)
print(e4 == e5)
#print(e4 is e5)
import copy
e6 = copy.copy(e4)
print("address of e4 {}".format(e4))
print("addresss of e6 {}".format(e6))

e6.name = "rohit"
print(e4.name)
print(e6.name)

class First:
    def __init__(self,name):
        a = 90
        b = 900
        c = a * b
        print(c)
        print(name)

obj = First('rohit')
obj1 = First('rohan')
obj2 = First
print(type(obj2))
print(type(First))

obj3 = obj2('rihit')
print("after creation object is {}".format(obj3))
'''
#del obj3
#print("after deletion object is {}".format(obj3))
#print(obj3)
'''
n = [1,2,3,4,10]
print 1,
print 2
'''
"""class Fruit:
    def cost_of_fruit(self):
        print("this will print cost of all fruits.")
    
    @classmethod
    def buy_fruit(cls):
        print("this is class method!")
     
    @staticmethod
    def add_into_cart():
        print("this is static method!")

ins = Fruit()
ins.cost_of_fruit()
#Fruit.cost_of_fruit()
Fruit.cost_of_fruit(ins)

Fruit.buy_fruit()
ins.buy_fruit()

Fruit.add_into_cart()
ins.add_into_cart()
"""
'''
class A:
    my_var = 9000
    def __init__(self,num):
        print(num)
        print("welcome to india!")
        
    def m1(self,a,b):
        self.var1 = a
        self.var2 = b
        print(a,b) 
           
    def m2(self):
        print(self.var1,self.var2)

obj = A(200)
obj1 = A(500)
obj.m1(5,8)
obj1.m1(7,9)
obj.m2()
print(obj.my_var)
print(obj1.my_var)
#obj.my_var = 4000
#print(obj.my_var)
print(obj1.my_var)
A.my_var = 4000
print(obj.my_var)
print(obj1.my_var)
'''
# Inheritance
"""class Employee:
    def __init__(self,f_name,l_name):
        self.f_name = f_name
        self.l_name = l_name
        print("first name is {}".format(self.f_name))
        print("last name is {}".format(self.l_name))

class Manager(Employee):
    def __init__(self,f_name,l_name,salary,job_grade):
        Employee
        self.salary = salary
        self.job_grade = job_grade
        print("salary is {} and job grade is {}".format(self.salary,self.job_grade))
"""              
#obj = Employee("rohit",'rohan')
#mn = Manager('rohan','mohan',100,'A')

"""class A:
    __name = "rohit"
    __age = 0
    
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age
    def get_age(self):
        return self.__age
    
obj = A()
#print(obj.__name)
print(obj.get_name())
obj.set_name('mohit')
obj.set_age(80)
print(obj.get_age())
print(obj.get_name())
"""
"""def my_func(var):
    print("before calling function")
    var()
    print("after calling function")
    var()

@my_func
def print_me():
    print("print my msg.")

@my_func
def print_msg():
    print("this one is differ.")
"""
"""
class A(object):
    def __init__(self):
        print("init called.")
        
    def __del__(self):
        print("del called.")
    
    
    def __str__(self):
        return "hi str called."
    
obj = A()
print(obj)    
obj1 = A()
"""    
    
    
    
        
        
        
        
        
        
        































































































































































































