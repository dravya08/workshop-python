# wapp to find fact of a number

num = int(input("enter the number "))
if num<0:
	print("b +ve")
elif num==0 or num == 1:
	print("fact = 1")
else:
	f = 1
	for i in range(1,num+1):
		f *= i
	print("fact =", f)