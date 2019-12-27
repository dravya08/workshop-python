'''
wapp tp read a sentence and sort every word of sentence
i/p Kamal sir rocks
o/p aaklm irs ckors''' 

s1= input("enter a string ")
l1= s1.split(" ")
ns1 =" "
for m in l1:
	m = m[::-1]
	ns1 = ns1 + " " + m



print("", ns1)