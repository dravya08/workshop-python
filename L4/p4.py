# wamdpp for stack implementation

import array
stack = array.array('i',[])

while True:
	op = int(input("1.push, 2.pop, 3.peek, 4.display and 5.exit "))
	if op == 1:
		ele = int(input("enter the element to push "))
		stack.append(ele)
		print(ele, "is pushed in stack ")
	elif op == 2:
		if len(stack) == 0:
			print("stack is empty ")
		else:
			ele = stack.pop()
			print(stack)
	elif op == 3:
		if len(stack) == 0:
			print("stack is empty ")
		else:
			ele = stack[-1]
			print("peeked element ", ele)
	elif op == 4:
		if len(stack) == 0:
			print("stack is empty ")
		else:
			print(stack)
		
	elif op == 5:
		break
	else:
		print("invalid option")