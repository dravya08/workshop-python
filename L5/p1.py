'''
wapp to process the following
s1 ="20,40,30,50,60,20"
perform addition of first three values

'''

s1 = "20 40 30 50 60 20"
d1 = s1.split(' ')

n1 = int(d1[0])
n2 = int(d1[1])
n3 = int(d1[2])

res = n1 + n2 + n3
print("res =", res )