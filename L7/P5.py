'''
wapp to count occurance of each word in given sentence 

'''
s1 = input("enter a string    ")
count = {}
s2 = s1.split(" ")

for s in s2:
	c = count.get(s,0)
	if c == 0:
		count[s] = 1
	else:
		count[s] = c + 1

print(count)


