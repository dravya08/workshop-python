''' wapp to accept n1 and n2 integers from Cla and perform res = n1 / n2	
	python p3.py 10 add 20
'''
import sys
try:
	n1 = int(sys.argv[1])
	op = sys.argv[2] 
	n2 = int(sys.argv[3])
	if op == "add":
		res = n1 + n2
	elif op == "sub":
		res = n1 - n2
	elif op == "mul":
		res = n1 * n2
	elif op == "div":
		res = n1 / n2
	else:
		print("invalid option")
	
	
except IndexError:
	print("enter minimum 2 integers")
except ValueError:
	print("enter a integer")
except ZeroDivisionError:
	print("no shud not be 0")
else:
	print("res =" ,res)
	

	
