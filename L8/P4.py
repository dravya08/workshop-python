class pcm:
	def __init__(self,p,c,m):
<<<<<<< HEAD
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



=======
		self.p=p	
		self.c=c
		self.m=m
	def show_pcm(self):
		print("physcis",self.p)
		print("chem",self.c)
		print("math",self.m)	

class nonpcm:
	def __init__(self,e,b):
		self.e=e
		self.b=b
	def show_nonpcm(self):
		print("eng",self.e)
		print("bio",self.b)

class marks(pcm,nonpcm):
	def __init__(self,p,c,m,e,b):
		pcm.__init__(self,p,c,m)
		nonpcm.__init__(self,e,b)
	def show(self):
		pcm.show(self)
		nonpcm.show(self)
	
m=marks(20,101,120,12,15)
m.show()
>>>>>>> 793662a638c2dd5f71ce99d367f71f83efeec3e5
