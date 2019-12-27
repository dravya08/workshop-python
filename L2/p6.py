# wapp to read three integers and find max of three

n1 = int(input("enter the first num "))
n2 = int(input("enter the second num "))
n3 = int(input("enter the third num "))

if(n1<n2):
	max = n1
else:
	max = n2
if(n3 > max):
	max = n3
print("max=",  max)
