# wapp to generate

num = int(input("enter the number "))
if num < 0:
	print("b +ve")
else:
	n = 0
	for i in range(1 , num+1):
		for j in range(1, i+1):
			print(n, end="")
			n = n + 1
		print()
