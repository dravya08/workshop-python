#wapp to read marks & find the grades 


mark = int(input("enter the marks "))
if (mark>=70):
	g="dist."
elif(mark>=60):
	g="FIRST CLASS"
elif(mark>=50):
	g="SECOND CLASS"
elif(mark>=40):
	g="PASS"
else:
	g="fail"

print("marks =", mark,"GRADES = ",g)


