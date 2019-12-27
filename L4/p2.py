# wapp to read marks of n students from the user and find
# 1.sum of marks 2.avg marks 3. highest marks 4. lowest marks

import array
num = array.array('i',[])

n = int(input("enter number of student "))
for i in range(n):
	ele = int(input("enter marks "))
	num.append(ele)

sum = 0
for n in num:
	sum = sum + n
avg =sum / len(num)

num = sorted(num)
max = num[-1]
min = num[0]

print("sum= ", sum)
print("avg= ", avg)
print("max= ", max)
print("min= ", min)

