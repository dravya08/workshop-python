class rectangle:
	def __init__(self,l,w):
		self.length = l
		self.width = w
	def show(self):
		print("length = ", self.length)
		print("width = ", self.width)
	def area(self):
		res = self.length * self.width
		print("area = ", res)
	def peri(self):
		res = 2 * self.length * self.width
		print("Peri = ", res)

length = float(input("Enter length "))
width = float(input("Enter width "))
r = rectangle(length, width)
r.show()
r.area()
r.peri()