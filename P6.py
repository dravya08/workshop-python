'''
create class mech with 
	IV : price
	
create class Bee with 
	IV : amount		

m=mech(500)
b=bee(500)

a1=m+b
a2=m-b
a3=b-m


'''


class mech:
	def __init__(self,price):
		self.price = price
	
	def __add__(self,other):
		res = self.price + other.amount
		return res
	def __sub__(self,other):
		res = self.price - other.amount
		return res

class bee:
	def __init__(self,amount):
		self.amount = amount
	def __sub__(self,other):
		res = self.amount - other.price
		return res


m=mech(500)
b=bee(350)

a1=m+b;  			print(a1);
a2=m-b;  			print(a2);
a3=b-m;  			print(a3);
	
