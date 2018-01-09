'''
Created on Jan 8, 2018

@author: kripa
'''

print(1+False)
print(bool(True))
print(bool(0))
print(bool(""))
print(bool("abc"))
print(bool([1,2,3,4]))
print(bool([]))
print(bool((1,2,3,4)))
print(bool(()))
print(bool({}))
print(bool({'name':'rohan'}))

if bool([]):
    print('hi')
else:
    print("no item available in list")
"""
num = 900
var = int(raw_input("enter the number you want to compare:"))
print(type(var))
if var > 900:
    print("greater then 900")
else:
    print("less then 900")
"""

name = "rohan"
age = 90
address = "blr"
if name == 'rohan' and age == 50 :
    print("welcome rohan")
elif age == 90 or address == 'blr':
    print("hello rohan")
else:
    print("thanks")
 
num  = 96 
print( 56 if num ==90 else 60 )




















    
    


