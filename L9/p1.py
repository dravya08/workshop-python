'''
wamdpp 1--> check if the given number is odd or odd 2 
	--> exit
'''

while True:
	try:
		op = int(input("1 check and 2 exit "))
		if op == 1:
			num = int(input("enter number to check "))
			if num % 2 == 0:
				print("even")
			else:
				print("odd")
		elif op == 2:
			break
		else:
			print("invalid option")
	except ValueError:
		print("u need to supply integers only")

		
		