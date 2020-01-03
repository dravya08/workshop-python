# wapp to delete a file whose name is supplied by the user

import os.path
file_name = input("enter filename to delete ")

if os.path.isfile(file_name):
	os.remove(file_name)
	print(file_name, "deleted")	
else:
	print(file_name, "does not exists ")