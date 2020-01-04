'''
wapp to read string and find occurence of each letter in the string

'''

count = {} 

s1 = input("enter name to add ")

for s in s1:
	c = count.get(s, 0)
	if c == 0:
		count[s] = 1
	else:
		count[s] = c + 1
print(count)
	


















