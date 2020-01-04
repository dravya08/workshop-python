#wapp to wish the user gm/ga/ge

import datetime

dt = datetime.datetime.now()
hour = dt.hour

if( hour >=6 and hour <=12):
	print("gm")
elif( hour >=12 and hour <=15):
	print("ga")
else:
	print("ge")
