# wapp to find the sum of first n positive integers
# eg i/p: 5 

n = int(input("enter the num "))

if n < 0:
	print("b +ve ")
else:
	sum = 0	
	i = 1
	while i < n:
		sum = sum + i
		i += 1
	else:
		print("sum of first", n , "=" , sum)