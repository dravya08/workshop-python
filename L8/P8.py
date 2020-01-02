class Book:
	def __init__(self,pages):
		self.pages = pages
	def __add__(kamal,other):
		res = kamal.pages + other.pages
		return Book(res)
	def __str__(self):
		return str(self.pages)
	
	

b1 = Book(100)
b2 = Book(400)
b3 = Book(300)

res = b1 + b2 + b3
print(res)

