'''
Created on Jan 8, 2018

@author: kripa
'''

a = 50
b = 100

a,b = b,a
print(a)
print(b)


my_list = (1,[2,3,4,5],90)
my_list[1][2] =900
print(my_list)


age  = 90
name = "rohan"
phone = ['656768','76787']
my_tupl = (1,2,3,4,5)
my_info = {'name':'rohit'}

result = age , name
print(result)
