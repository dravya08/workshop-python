''' 
create class mech with iv- price
create class bee with iv - amount
m = Mech(500)
b = Bee(350)
a1 = m + b; 		print(a1);
a2 = m - b; 		print(a2);
a3 = b - m; 		print(a3);
'''
class Mech:
	def __init__(self,price):
		self.price = price
	def __add__(self,other):
		res = self.price + other.amount
		return res
	def __sub__(self,other):
		res = self.price - other.amount
		return res
	

class Bee:
	def __init__(self,amount):
		self.amount = amount
	def __sub__(self,other):
		res = self.amount - other.price
		return res

m = Mech(500)
b = Bee(350)

a1 = m + b;	print(a1)
a2 = m - b; 	print(a2)
a3 = b - m; 	print(a3)
	
	
	