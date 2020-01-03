import threading
import time
def even():
	print("even started ")
	for i in range(1, 21):
		if i % 2 == 0:
			print("even ", i)
		time.sleep(0)
def odd():
	print("odd started")
	for i in range(1, 21):
		if i%2 != 0:
			print("odd " ,i)
		time.sleep(0)
print("aate hi kam shuru kar diye")
a = threading.Thread(target=odd)
m = threading.Thread(target=even)
a.start()
m.start()
a.join()
m.join()
print("har bar garam kar k chod dayta ho")