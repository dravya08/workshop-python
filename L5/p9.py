# wapf t find factorial of a number

def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1) 

num = int(input("enter a number "))
if num < 0:
	print("b+ ve")
elif num == 0 or num == 1:
	print("fact = 1")
else:
	res = fact(num)
	print(res)
