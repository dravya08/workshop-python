'''
wapp to read tuple of integers from the user & print in descending
'''

list_data  = []
tuple_data = ()
reply = input("do u wish to add integers y/n ")
while reply == 'y':
	ele = input("enter no to add ")
	list_data.append(ele)
	reply = input("do u wish to more np y/ n ")

tuple_data = tuple(list_data)
print("Original data", tuple_data)

list_data.sort(reverse =True)

tuple_data = tuple(list_data)
print("Sorted data", tuple_data)





