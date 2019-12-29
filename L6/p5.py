# wapp to read list of integers from the user
# create two list even_list and odd_list

data = []
reply = input("do u wish to add elements y/n ")
while reply == 'y':
	ele = int(input("enter element to add "))
	data.append(ele)
	reply = input("do u wish to more elements y/ n ")

print(data)
