
# wapp to write data into an existing file

import os.path
file_name = input("enter filename to create ")

if os.path.exists(file_name):
	f = None
	try:
		f = open(file_name, "a")
		data = input("enter data to write ")
		f.write(data + "\n")
		print("writing done ")
	except Exception as e:
		print("issue", e)
	finally:
		if f is not None:
			f.close()
else:
	print(file_name,"file does not exists ")
  
	print(file_name, "does not exits")
