import threading
import time
def even():
	print("even numbers started")
	for i in range(1,21):
		if i%2 == 0:	
			print(i,"even number  ")
		time.sleep(0.5)

def odd():	
	print("odd numbers started:")
	for i in range(1,20):
		if i%2 != 0:	
			print(i,"odd number")
		time.sleep(0.5)


print("aaj ka kaam shuru")
a = threading.Thread(target= even)
m = threading.Thread(target=odd)
a.start()
m.start()
a.join()
m.join()
print("aaj ka kaam khatam")

