'''
Created on Jan 9, 2018

@author: kripa
'''
''''i = 0
while i <10:
    print('hello') 
    print("valoue of i is {}".format(i))
    i +=1
    
print("exit")

para = "this is a boy."
index = 0
while index < len(para):
    print(para[index])
    index +=1
    
my_list = [1,2,3,4,5]
var = 0
while var <len(my_list):
    print(my_list[var]*my_list[var])
    var +=1

my_tuple = ('apple','banana','mango')

user_data = {'username':'rohit',
             'password':'blr@456'
             }
uname = raw_input("Enter user name:")
pwd = raw_input("enter password:")

while  pwd != user_data['password'] or uname != user_data['username']:
    print("username and pasword incorrect ")
    uname = raw_input("Enter user name:")
    pwd = raw_input("enter password:")
print("login success.")'''


'''
print(range(12))
var = range(2,101,2)
print(type(var))
print(var)
'

for i in range(10):
    print(i)
    
count = 1    
for i in range(1,20,2):
    print("loop execution count {}".format(count))
    count +=1
    print(i)

para = "Ram goes to market."

for i in range(5,len(para)-2):
    print(para[i])

fruits = ['apple','banana','mango']
for i in range(len(fruits)):
    print(fruits[i])
    
numbers = (3,4,5,6,7,8)
result = []
for i in range(len(numbers)):
    result.append(numbers[i]*numbers[i]*numbers[i])
print(result)


for i in range(10):
    print("before break stmnt i is {}".format(i))
    if i == 3:
        break
    print("after break stmnt i is {}".format(i))
'
for i in range(10):
    print("before continue {}".format(i))
    if i == 2:
        continue
    print("after continue i {}".format(i))

num = 90
if num == 80:
    pass

my_list   = [[8,9,10],[11,12,13],[14,15,16]]

for i in range(len(my_list)):
    print(my_list[i])
    for j in range(len(my_list[i])):
        print(my_list[i][j])

complex_list = [[[1,2,3],[4,5,6]],[[4,5,6],[7,8,9]]]
print("len of complex list is {}".format(len(complex_list)))
for i in range(len(complex_list)):
    print("elemnet of a list is  {} at index {}".format(complex_list[i],i))   
    for j in range(len(complex_list[i])):
        print("elemnet of b list is  {} at index {}".format(complex_list[i][j],j))
        for k in range(len(complex_list[i][j])):
            print("elemnet of c list is  {} at index {}".format(complex_list[i][j][k],k))
'''        
    











































































































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    