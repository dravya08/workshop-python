# wapp to write data into an existing file

import os.path
file_name = input("enter filename to write ")

if os.path.exists(file_name):
	f = None
	try:
		f = open(file_name, "a")
		data = input("enter data to write press q for quit ")
		while data != 'q':
			f.write(data + "\n")
			data = input()
		print("writing done ")
	except Exception as e:
		print("issue", e)
	finally:
		if f is not None:
			f.close()
else:
	print(file_name, "does not exits")