'''
wapf called myrange() to which we can pass 1 or 2 parameters
1 parameter wub be considered as stop value
2 parameters wud be considered as start and stop
'''
def myrange(p1,p2=None):
	if p2 is None:
		i = 0
		while i<= p1:
			print(i)
			i += 1
	if p2 != None:
		for i in range(p1,p2):
			print(i)

myrange(10)
myrange(3,15)
			
	
			