'''
Created on Jan 4, 2018

@author: kripa
'''
my_dict = {}
print(type(my_dict))
my_dict = {'name':'rohan','age':39,'address':'blr'}
print(my_dict)
print(my_dict['name'])

'''my_data = {34 : "blr" ,
           'name': 'rohit',
           (1,2,3) : "delhi",
           {'age':70}:"bye"
           }
print(my_data[34])
print(my_data['name'])
print(my_data[(1,2,3)])
#print(my_data[{'age':70}])'''

my_data = {
           'age':90,
           'name':'rohit'}
print(my_data['age'])
print(my_data['name'])

my_list = [1,2,3,4,5,'apple']
my_data['listInfo'] = my_list
print(my_data)
print(my_data['listInfo'])

my_tup = (1,2,3,4,5)
my_data['tupInfo'] = my_tup
print(my_data)
print(my_data['tupInfo'])
              
              
my_data = {
           'emp_1': {'name':'vipul',
                     'age':90,
                     'address':'blr'},
           'emp_2':{"name":"rohit",
                    'age':45,
                    'address':'delhi'
                    },
           'region':'india'
           }
print(my_data['emp_1']['name'])
print(my_data.has_key('region'))
print(my_data.has_key('india'))

my_info = {'name':'vipul','age':24}
print(my_info.items())
print(my_info.pop('age'))
print(my_info)
print(my_data.keys())
print(my_data.values())
##############################

name = raw_input("Enter any name:")
phoneNumber = raw_input("Enter phone number :")

info = {'name':name,
        'phoneNumber':phoneNumber}
print(info)



































