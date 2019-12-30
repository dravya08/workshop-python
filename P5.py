class Book:
	def __init__(self,nop):
		self.nop = nop
	def __add__(self,other):
		res = self.nop + other.nop
		return res
	def __sub__(kamal,kajal):
		res = kamal.nop - kajal.nop
		return res


b1=Book(100)
b2=Book(200)

res=b1+b2
print(res)
	
ares=b1-b2
print(ares)
