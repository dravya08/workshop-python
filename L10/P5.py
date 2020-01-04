#wapp to read from a file whose name is supplied by the user


import os.path
file_name = input("enter the file_name to read ")

if os.path.isfile(file_name):	
	f = None
	try:
		f = open(file_name,'r')
		data=f.read()
		print(data)
	except Exception as e:
		print("issue",e)
	finally:
		if f is not None:
			f.close()
		print("reading done")
else:
	print(file_name,"file does not exists ")

