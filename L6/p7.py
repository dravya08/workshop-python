# wapp to read list of names & create a list of unique names

data = []
reply = input("do u wish to add names y/n ")
while reply == 'y':
	ele = input("enter name to add ")
	data.append(ele)
	reply = input("do u wish to more names y/ n ")

new_data = []
for d in data:
	if d not in new_data:
		new_data.append(d)

print("og list",data)
print("new list",new_data)