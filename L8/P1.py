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

id = int(input("Enter emp id ")) 
name = input("Enter emp name ")
salary = float(input("Enter emp salary "))
e = employee(id,name,salary)
e.show()
e.calc_bonus()

		
	