'''
Created on Jan 11, 2018

@author: kripa
'''
"""

def printer(msg):
    print(msg)
    #print("blr")
#printer("hi")
#printer("hello")

def mult(a,b):
    c = a*b
    #return c
    
    
var  = mult(3, 4)
print(var)

#direct Call
printer("blr")

# Indirect call
print_msg = printer
print_msg("delhi")

print(print_msg.__name__)

next_alias = print_msg

print(next_alias.__name__)



def function_one(a,b,c): return a+b+c
result = function_one(3, 6, 8)
print(result)


def fact(a):
    #fact(a)
    if a == 0:
        return 1
    else:
        return a*fact(a-1)
print(fact(5))

def my_function(x,y,z): return x+y+z
var =my_function(4, 6, 9) 
print(var)

var = (lambda x,y,z: x+y+z)
print(type(var))
print(var(2,4,6))

calc = {'add':(lambda x,y:x+y),
        'mult':(lambda x,y:x*y),
        'sub':(lambda x,y:x-y)}
var1 = int(raw_input("enter first number:"))
var2 = int(raw_input("enter second number:"))
opt = raw_input("enter opration:")
print(calc[opt](var1,var2))
"""
# generators

my_list_data = [1,2,3,4,5,6]
def my_gen(var):
    for i in var:
        yield i*i
obj = my_gen(my_list_data)
print(type(obj))
#print(next(obj))
#print(next(obj))
#print(next(obj))
for i in obj:
    print(i)













