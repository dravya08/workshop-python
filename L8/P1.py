'''
waoopp for class employee :
	SV: company_name = 'tcs'
	IV: eid,ename,esalary
	PI: for eid,ename,esalary
	IM: show() to display employee info with cimoany_name
	IM: calc_bonus to display bonus amount which is 20% of salary
	do create a object forr testing purpose
'''

class employee:
	company_name = 'TCS'
	def __init__(self,i,n,s):
		self.eid = i
		self.ename = n
		self.esalary = s
	def show(self):
		print("id",self.eid)
		print("name",self.ename)
		print("salary",self.esalary)
		print("company name:",employee.company_name)

	def calc_bonus(self):
		amount = self.esalary * 0.20
		print("Bonus amount",amount)

id = int(input(" enter id "))
name = input(" enter name ")
salary = float(input(" enter salary "))
e = employee(id, name , salary)
e.show()
e.calc_bonus()






