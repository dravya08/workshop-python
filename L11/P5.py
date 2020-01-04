# wappp to ask user for dob and find the birthday

import datetime
try:
	year = int(input("Enter year "))	
	
	month = int(input("Enter Month "))
	day = int(input("Enter day "))
	dob = datetime.date(year,month,day)
	print(dob)
	days_in_year = 365.2425    
	dt = datetime.datetime.now().date()
	age = (dt - dob) / datetime.timedelta(days=365)
	print("approx age= ", age)
	diff = dt - dob
	print("days=", diff)
	
except ValueError as e:
	print("Input issue", e)	
