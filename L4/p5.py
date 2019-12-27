# wamdpp for queue implementation

import array
queue = array.array('i',[])

while True:
	op = int(input("1.insert, 2.remove, 3.peek, 4.display and 5.exit "))
	if op == 1:
		ele = int(input("enter the element to insert "))
		queue.append(ele)
		print(ele, "is inserted in queue ")
	elif op == 2:
		if len(queue) == 0:
			print("queue is empty ")
		else:
			ele = queue.pop(0)
			print("removed element is", ele)
	elif op == 3:
		if len(queue) == 0:
			print("queue is empty ")
		else:
			ele = queue[0]
			print("peeked element ", ele)
	elif op == 4:
		if len(queue) == 0:
			print("queue is empty ")
		else:
			print(queue)
		
	elif op == 5:
		break
	else:
		print("invalid option")