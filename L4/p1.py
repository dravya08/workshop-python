# wapp to read array from the user and print on the screen

import array
num = array.array('i',[])

n = int(input("enter number of elements "))
for i in range(n):
	ele = int(input("enter elements "))
	num.append(ele)

print(num)
for n in  num:
	print(n, end=' ')
print()

for i in range(len(num)):
	print(num[i], end =' ')
print()

