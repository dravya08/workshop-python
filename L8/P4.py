class pcm:
	def __init__(self,p,c,m):
		self.p = p
		self.c = c
		self.m = m

	def show_pcm(self):
		print("physics ", self.p)
		print("chemistry", self.c)
		print("maths", self.m)

class nonpcm:
	def __init__(self,e,b):
		self.e = e
		self.b = b
	
	def show_nonpcm(self):
		print("english", self.e)
		print("biology", self.b)

class marks(pcm, nonpcm):
	def __init__(self,p,c,m,e,b):
		pcm.__init__(self,p,c,m)	#Super nahi aayega multiple inheritance 
		nonpcm.__init__(self,e,b)	#class name layne padega with self

	def show(self):
		super().show_pcm()
		super().show_nonpcm()

m = marks(99,77,88,99,99)
m.show()



