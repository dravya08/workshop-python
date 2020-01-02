<<<<<<< HEAD
''' waoop for class employee:
	SV: company_name = 'TCS'
	IV: eid,ename, esalary
	PI: for eid, ename , esalary
	IM: show() to display employee info with company
	IM: calc_bonus() to display bonus amount which is 20% of salary
	do create a object for testing purpose'''
=======
'''
waoopp for class employee :
	SV: company_name = 'tcs'
	IV: eid,ename,esalary
	PI: for eid,ename,esalary
	IM: show() to display employee info with cimoany_name
	IM: calc_bonus to display bonus amount which is 20% of salary
	do create a object forr testing purpose
'''
>>>>>>> 793662a638c2dd5f71ce99d367f71f83efeec3e5

class employee:

	company_name = "TCS"
<<<<<<< HEAD
	def __init__ (self,id,name,salary):
		self.id = id
		self.name = name 
		self.salary = salary
=======
	def __init__ (self,i,n,s):
		self.id = i
		self.name = n
		self.salary = s
>>>>>>> 793662a638c2dd5f71ce99d367f71f83efeec3e5
	
	def show(self):
		print("Id: ",self.id)
		print("Name: ", self.name)
		print("Salary: ", self.salary)
		print("Company Name: ",employee.company_name)
	
	def calc_bonus(self):
		amount = self.salary * 0.20
		print("Bonus amount ",amount)

class salesperson(employee):
	def __init__(self,i,n,s,c):
		super().__init__(i,n,s)
		self.comm = c
	def show(self):
		super().show()
		print("comm= ",self.comm)

id = int(input("Enter emp id ")) 
name = input("Enter emp name ")
salary = float(input("Enter emp salary "))
comm = float(input("enter comm "))
sp = salesperson(id,name,salary,comm)
sp.show()
sp.calc_bonus()

<<<<<<< HEAD
		
	
=======











>>>>>>> 793662a638c2dd5f71ce99d367f71f83efeec3e5
