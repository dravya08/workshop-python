# wapf t find fibo of a number

def fact(n):
	f = 0
	for i in range(1,n+1):
		f+= i
	return f

num = int(input("enter a number "))
if num < 0:
	print("b+ ve")
elif num == 0 or num == 1:
	print("fact = 1")
else:
	res = fact(num)
	print(res)
