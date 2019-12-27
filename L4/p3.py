# wapp to read marks of n integer from the user and display
# 1. no of +ve ele 2. -ve 3. O's


import array
num = array.array('i',[])

n = int(input("enter number of integer "))
for i in range(n):
	ele = int(input("enter integers "))
	num.append(ele)

np, nn , nz = 0,0,0

for e in num:
	if(e > 0):
		np += 1
	elif(e < 0):
		nn += 1
	else:
		nz += 1
print("postive",np ,"negative", nn ,"zero", nz)	



