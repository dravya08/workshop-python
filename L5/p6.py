'''
wapp tp read a sentence and sort every word of sentence
i/p Kamal sir rocks
o/p aaklm irs ckors'''

def mysort(s):
	ls = sorted(s)
	ns = ''.join(ls)
	return ns 

s1= input("enter a string ")
l1= s1.split(" ")
ns1 =" "
for m in l1:
	m = mysort(m)
	ns1 = ns1 + " " + m



print("", ns1)