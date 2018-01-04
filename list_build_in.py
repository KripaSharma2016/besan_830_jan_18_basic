'''
Created on Jan 3, 2018

@author: kripa
'''
l1 = []
print(type(l1))
my_list  = list()
print(my_list)
print(type(my_list))
my_list.append("rohan")
my_list.append(123)
print(my_list)
my_list.append("ram")
print(my_list)
my_list.append(78.90)
print(my_list)

my_list = ["rohan",1234]
print(my_list[0][1:3])


new_list = [4,6,7,2,1,3,3,5,6]
print(new_list.count(3))

list_one = [1,2,3]
list_two = [4,5,6,7]
list_three = []
list_three.append(list_one)
list_three.append(list_two)
print(list_three)
print(len(list_three))
list_four = []
list_four.extend(list_one)
list_four.extend(list_two)
print(list_four)
print(len(list_four))

















