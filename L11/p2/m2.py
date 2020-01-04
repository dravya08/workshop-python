class c2:
	def ssv_to_csv(self,s1):
		data = s1.split(" ")
		r1 =','.join(data)
		return r1


	def csv_to_ssv(self,s2):
		data = s2.split(",")
		r2 =' '.join(data)
		return r2