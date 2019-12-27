# wapp to read year & find if its a leap year

year = int(input("Enter the year"))

b1 = (year%100 == 0) and (year%400 == 0)
b2 = (year%100 != 0) and (year%4 == 0)

if b1 or b2:
	print("yessssssss")
else:
	print("naaaaaaa")