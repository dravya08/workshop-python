'''
wapp to check if the given string is "palindrome"
'''


s1 = input("Enter the string ")
r1= s1[::-1]

if s1==r1:
	print("Yess")
else:
	print("noonono")
