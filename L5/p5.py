'''
wapp to check if given string are anagrams
s1 = listen 
s2 = silent
'''
def mysort(s):
	ls = sorted(s)
	ns = ''.join(ls)
	return ns

s1 = input("enter first string ")
ns1 = mysort(s1)
s2 = input("enter second string ")
ns2 = mysort(s2)


if ns1 == ns2:
	print("anagram")
else:
	print(" no anagram")
