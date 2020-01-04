'''#wapp to write multiple lines into a file whose name is supplied by the user

mine code

import os.path
file_name = input("enter the file_name to write ")

if os.path.isfile(file_name):	
	f = None
	try:
		f = open(file_name,'a')
		reply = input("do u wish to add data y/n ")
		while reply == 'y':
			data = input("enter data to write ")
			f.write(data + "\n")
			reply = input("do u wish to add more data y/n ")
		print("writing done ")
	except Exception as e:
		print("issue",e)
	finally:
		if f is not None:
			f.close()
else:
	print(file_name,"file does not exists ")
'''


import os.path
file_name = input("enter the file_name to write ")

if os.path.isfile(file_name):	
	f = None
	try:
		f = open(file_name,'w')
		data = input("enter data to write press q for quit ")
		while data!= 'khatam':
			f.write(data + "\n")
			data=input()
		print("writing done ")
	except Exception as e:
		print("issue",e)
	finally:
		if f is not None:
			f.close()
else:
	print(file_name,"file does not exists ")

