import threading
import time
def work():
	print("writing started")
	for i in range(1,5):
		print("writing ", i, "assignment")
		time.sleep(0.5)
	print("writing ended")
def music():	
	print("music started:")
	for i in range(20):
		print("music ", i, "assignment")
		time.sleep(0.5)
	print("music ended")

print("aaj ka kaam shuru")
a = threading.Thread(target= work)
m = threading.Thread(target=music)
a.start()
m.start()
a.join()
m.join()
print("aaj ka kaam khatam")

