# wapp to read list of integers from the user
# create two list even_list and odd_list

data = []
reply = input("do u wish to add elements y/n ")
while reply == 'y':
	ele = int(input("enter element to add "))
	data.append(ele)
	reply = input("do u wish to more elements y/ n ")
even =[]
odd = []
for d in data:
	if d%2 == 0:
		even.append(d)
	else:
		odd.append(d)
print("orginal list",data)
print("even list",even)
print("odd", odd)
