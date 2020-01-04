#wapp to write into a file whose name is supplied by the user

import os.path
file_name = input("enter the file_name to create ")

if os.path.isfile(file_name):	
	f = None
	try:
		f = open(file_name,'w')
		data = input("enter data to write ")
		f.write(data+"\n")
		print("writing done ")
	except Exception as e:
		print("issue",e)
	finally:
		if f is not None:
			f.close()
else:
	print(file_name,"file does not exists ")
