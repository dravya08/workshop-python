'''
#wapp to delete a file whose name is supplied by thte user

mine code

import os.path
file_name = input("enter the file_name to delete ")

if os.path.exists(file_name) == False:	
	print(file_name,"file does not exists")
else:
	os.remove(file_name)
	print(file_name,"Deleted")

'''

'''sir ka code'''
#wapp to delete a file whose name is supplied by thte user

import os.path
file_name = input("enter the file_name to delete ")

if os.path.isfile(file_name):	
	os.remove(file_name)
	print(file_name,"Deleted")
else:
	print(file_name,"file does not exists")
