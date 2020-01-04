'''

create class employee with IV:- id name,pds (per day salary ) 
create class attendance with :- IV nodp (no. of days present)

e = employee(10,"amit",500)
a = attendance(23)

salary = e*a ;print(salary)

'''


class employee:
	def __init__(self,id,name,pds):
		self.i = id
		self.name = name 
		self.pds = pds
	def __mul__(self,other):
		res = self.pds * other.nodp
		return res
class attendance:
	def __init__(self,nodp):
		self.nodp = nodp


e = employee(10,"amit",500)
a = attendance(23)

salary = e * a 
print(salary)
