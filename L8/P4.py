class pcm:
	def __init__(self,p,c,m):
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
