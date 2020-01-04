'''
wapp to read two set of names:
1.Java student names
2 python student names

find 	1. names of all student
	2. names of common student
	3. students in java not in python
'''

java = set()
python = set()
# read java names
reply = input("do u wish to add java names y/n ")
while reply == 'y':
	ele = input("enter name to add ")
	java.add(ele)
	reply = input("do u wish to more java names y/ n ")

# read python names
reply = input("do u wish to add python names y/n ")
while reply == 'y':
	ele = input("enter name to add ")
	python.add(ele)
	reply = input("do u wish to more python names y/ n ")

# perform set operation
print("Total students",(java | python))

print("Common names",(java & python ))

print("Students in java but no python",(java - python))
















