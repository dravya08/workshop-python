import os.path
import pickle

class student:
	def __init__(self,rno,name):
		self.rno = rno
		self.name = name
	def __str__(self):
		msg = "rno= " + str(self.rno) + " name= " + str(self.name)
		return msg

stu = []
file_name = "student_ka_data.ser"
if os.path.exists(file_name):
	f = open(file_name, "rb")
	stu = pickle.load(f)
	f.close()

while True:
	op = int(input("1.add 2.view 3.delete and 4.exit  "))
	if op == 1:
		rno = int(input("enter rno "))
		name = input("enter name ")
		s = student(rno, name)
		stu.append(s)
		print("object saved in the list")
	elif op == 2:
		for s in stu:
			print(s)
	elif op == 3:
		ele = int(input("enter the rno to delete "))
		for s in stu:
			if s.rno == ele:
				stu.remove(s)
				print("record deleted")
	elif op == 4:
		f =open(file_name, "wb")
		pickle.dump(stu,f)
		f.close()
		break
	else:
		print("invalid option")


















