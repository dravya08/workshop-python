'''
	wapp to accept n1 and n2 integers from CLA and perform res = n1+n2
'''
	
import sys
try:
	n1=int(sys.argv[1])
	n2=int(sys.argv[2])
	res=n1/n2
except IndexError:
	print("provide input")
except ValueError:
	print("provide integers only")
except ZeroDivisionError:
	print("second number can't be zero")
else:
	print("res=", res)


