class circle:
	def __init__(self,r):
		self.radius = r
	def show(self):
		print("radius = ", self.radius)
	def area(self):
		res = 3.14 * self.radius * self.radius
		print("area = ", res)
	def circum(self):
		res = 2 * 3.14 * self.radius
		print("circum = ", res)

radius = float(input("Enter Radius "))

r = circle(radius)
r.show()
r.area()
r.circum()