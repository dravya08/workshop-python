# wapp to accept n1 and n2 integers from Cla and perform res = n1 / n2

import sys

try:
	n1 = int(sys.argv[1])
	n2 = int(sys.argv[2])
	res = n1 / n2

except IndexError:
	print("enter minium 2 integers")
except ValueError:
	print("enter a integer")
except ZeroDivisionError:
	print("no shud not be 0")
else:
	print("res= ", res)
	
