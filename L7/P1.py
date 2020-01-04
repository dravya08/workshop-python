'''
wapp to read list of names and find the name having the maximum no of letters 
dog cat batman dinosaur monkey
'''

names  = []
reply = input("do u wish to add names y/n ")
while reply == 'y':
	ele = input("enter name to add ")
	names.append(ele)
	reply = input("do u wish to more names y/ n ")

max = len(names[0])
for n in names:
	if len(n) > max:
		max = len(n)

for n in names:
	if len(n) == max:
		print(n,end="")



