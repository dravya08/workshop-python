'''
Wapf to return True if the given no. is Armstrong number else False

def arm(n1):
	n = order(n1)
	temp = n1
	sum != 0
	while temp != 0:
		r = temp% temp
		sum1 += power(r,n)
		temp /= 10
		
	return sum1 == n1
	
n1 = 153
print(arm(n1))
'''
	
def check(num):
	org_num = num
	sum = 0
	while num> 0:
		digit = num % 10
		sum += digit ** 3
		num //= 10
	if org_num == sum:
		return True
	else:
		return False

num = int(input("enter a number to check "))
if check(num):
	print("Yessss")
else:
	print("Nooooooo")		