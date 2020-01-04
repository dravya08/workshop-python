'''
wamdpp 1--> check if the given number is even or odd 2-->
'''


while True:
	
	try :
		op = int(input("1 check and 2 exit "))
		if op == 1:
			num = int(input("enter the number to check "))
			if num%2==0:
				print("even")
			else:
				print("odd")
		elif op == 2:
			break
		else:
			print("Invalid Option ")
	except ValueError:
			print("Enter integer only ")
