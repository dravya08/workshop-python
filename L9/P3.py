'''

''''''
	wapp to accept n1 and n2 integers from CLA and perform res = n1 and/sub/mul/div n2
'''
	
import sys
try:
	n1=int(sys.argv[1])
	op=sys.argv[2]	
	n2=int(sys.argv[3])
	if op =='add':	
		res=n1+n2
	elif op =='sub':
		res=n1-n2
	elif op =='mul':
		res=n1*n2
	elif op =='div':
		res=n1/n2
	else:
		print("invalid option")
except IndexError:
	print("provide input")
except ValueError:
	print("provide integers only")
except ZeroDivisionError:
	print("second number can't be zero")
else:
	print("res=", res)

