#wapp to find the age of the user

import datetime
try:
	year = int(input("enter your year "))
	month = int(input("enter your month "))
	day = int(input("enter your day "))

	dob = datetime.date(year,month,day)
	print(dob)

	today = datetime.datetime.now().date()
	diff = today - dob
	print("days = ",diff)
	dt = datetime.datetime.now().date()
	age = (dt-dob)/datetime.timedelta(days=365)
	print("approx age:",round(age,2))	

except ValueError as e:
	print("input issue",e)
