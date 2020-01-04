import threading
import time
class Assignments(threading.Thread):
	def run(self):
		print("writing started ")
		for  i in range(1,11):
			print("writing ", i ,"assignment")
			time.sleep(3)
		print("writing ended")
class Music(threading.Thread):
	def run(self):
		print("Music started ")
		for i in range(1, 21):
			print("song " ,i , "played")
			time.sleep(1)
		print("Music stopped")
print("aate hi kam shuru kar diye")
a = Assignments()
m = Music()
a.start()
m.start()
a.join()
m.join()
print("har bar garam kar k chod dayta ho")
