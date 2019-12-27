# wapp to generate


num = int(input("enter the number "))
if num < 0:
	print("b +ve")
else:
	n = 65
	for i in range(num , 0 ,-1):
		print((str(chr(n))+"\t") * i)
		n = n + 1
