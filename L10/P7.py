import threading
import time
class Assignments(threading.Thread):
	def run(self):
		print("writing started")
		for i in range(1,5):
			print("writing ", i, "assignment")
			time.sleep(3)
		print("writing ended")
class Music(threading.Thread):
	def run(self):	
		print("music started:")
		for i in range(20):
			print("music ", i, "assignment")
			time.sleep(1)
		print("music ended")

print("aaj ka kaam shuru")
a = Assignments()
m = Music()
a.start()
m.start()
a.join()
m.join()
print("aaj ka kaam khatam")

