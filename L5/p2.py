'''
wapp to process the following
s1 ="a,2,b,4,c,3"
a a 
b b b b
c c c

'''

s1 = "a,2,b,4,c,3"
d1 = s1.split(',')

for i in range(0,len(d1),2):
	what = d1[i]
	how = int(d1[i+1])
	print((what+"\t") * how)

