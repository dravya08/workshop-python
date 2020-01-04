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
	
def check(num, p):
	org_num = num
	sum = 0
	while num> 0:
		digit = num % 10
		sum += digit ** p
		num //= 10
	if org_num == sum:
		return True
	else:
		return False


for i in range(100,1000):
	if check(i, 5): # p ka value
		print(i)		