# wapp to read data into an existing file

import os.path
file_name = input("enter filename to read ")

if os.path.exists(file_name):
	f = None
	try:
		f = open(file_name, "r")
		data = f.read()
		print(data)
	except Exception as e:
		print("issue", e)
	finally:
		if f is not None:
			f.close()
		print("*** reading done ***")
else:
	print(file_name, "does not exits")