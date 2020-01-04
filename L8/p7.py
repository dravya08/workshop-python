'''
create class Employee with Iv - id,name,pds(per day salary)
create class Attendace with Iv - nodp (no of days present)
e =Employee(10,"Amit",500)
a = Attendance(23)
'''

class Employee:
	def __init__(self,id,name,pds):
		self.id = id
		self.name = name
		self.pds = pds
	def __mul__(self,other):
		res = self.pds * other.nodp
		return res
	

class Attendance:
	def __init__(self,nodp):
		self.nodp = nodp




e = Employee(10,"Amit",500)
a = Attendance(23)
salary = e * a
print(salary)	