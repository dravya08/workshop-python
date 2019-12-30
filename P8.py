class Book:
	def __init__(self,pages):
		self.pages=pages
	def __add__(self,other):
		res = self.pages + other.pages
		return Book(res)
	def __str__(self):
		return str(self.pages)
	
b1 = Book(200)
b2 = Book(300)
b3 = Book(100)

ans = b1+b2+b3
print(ans)
