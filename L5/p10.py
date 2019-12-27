#wapp to find the sum of digits

def sod(n):
	sum = 0
	while n>0:
		digit = n % 10
		sum += digit
		n //= 10
	return sum

num = int(input("enter a number"))
if num< 0:
	print("b +ve")
else:
	res = sod(num)
	print("sum=", res)