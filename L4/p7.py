'''
wapp to read a string and count the number of vowels and consonants



'''
s1 = input("Enter a string ")
vc, cc= 0,0

for s in s1:
	if s.isalpha():
		if s in ['a','e','i','o','u','A','E','I','O','U']:
			vc+= 1
		else:
			cc+=1
	else:
		print("enter valid")
print("vowels:", vc,"consonants:",cc)

