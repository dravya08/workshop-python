# wapp to wish the user gm/ga/ge

import datetime

dt = datetime.datetime.now()
hour = dt.hour

<<<<<<< HEAD
if (hour >= 6 and hour <= 12):
	print("Good Morning")
elif (hour >= 12 and hour <= 15):
	print("Good Afternoon")
else:
	print("Good Evening")
=======
if( hour >=6 and hour <=12):
	print("gm")
elif( hour >=12 and hour <=15):
	print("ga")
else:
	print("ge")
>>>>>>> d3c60527e310894c4689c921642c8aca2c98676d
