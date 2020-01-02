''' waoop for class employee:
	SV: company_name = 'TCS'
	IV: eid,ename, esalary
	PI: for eid, ename , esalary
	IM: show() to display employee info with company
	IM: calc_bonus() to display bonus amount which is 20% of salary
	do create a object for testing purpose'''

class employee:

	company_name = "TCS"
	def __init__ (self,id,name,salary):
		self.id = id
		self.name = name 
		self.salary = salary
	
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
	def calc_bonus(self):
		amount = self.esalary * 0.50
		print("bonus amount", amount)

id = int(input("Enter emp id ")) 
name = input("Enter emp name ")
salary = float(input("Enter emp salary "))
comm = float(input("enter comm "))
sp = salesperson(id,name,salary,comm)
sp.show()
sp.calc_bonus()

		
	