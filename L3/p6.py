# wapp to read two range r1 and r2 from the user
# if n is multiple of 3 o\p="amar"
# if n is multiple of 5 o\p="akbar"
# if n is multiple of 7 o\p="anthony"



r1 = int(input("enter 1 range "))
r2 = int(input("enter 2 range "))

for i in range(r1,r2):
	if(i%3==0 and i%5== 0):
		print("anthony")
	elif(i%3 == 0):
		print("amar")
	elif(i%5 == 0):
		print("akbar")

