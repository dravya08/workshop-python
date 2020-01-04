#wapp to create a file whose name is supplied by thte user

import os.path
file_name = input("enter the file_name to create ")

if os.path.exists(file_name):	
	print(file_name,"aleady exists")
else:
	f = None
	try:
		f = open(file_name,'a')
		print(file_name,"created")
	except Exception as e:
		print("issue",e)
	finally:
		if f is not None:
			f.close()
