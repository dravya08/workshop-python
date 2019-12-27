'''
wapp to read a string and count the number of letters, digits and other characters
eg i/p: kam1 23a$$ o/p letters 4 digits 3 other 3



'''
s1 = input("Enter a string ")
lc, dc, oc= 0,0,0

for s in s1:
	if(s.isalpha()):
		lc+= 1
	elif(s.isdigit()):
		dc+= 1
	else	:
		oc+= 1
print("letters", lc,"digits",dc,"others",oc)

