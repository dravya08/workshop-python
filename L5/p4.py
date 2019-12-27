'''
wapp to check if given string are anagrams
s1 = listen 
s2 = silent
'''
s1 = input("enter first string ")
s2 = input("enter second string ")

ls1= sorted(s1)
ls2= sorted(s2)

if(ls1 == ls2):
	print("anagram")
else:
	print(" no anagram")
