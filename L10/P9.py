import threading
import time
balance = 500
s = threading.Semaphore()

def deposit():
	print("deposting started ")
	s.acquire()
	global balance
	amt1 = balance
	time.sleep(2)
	amt1 += 100
	balance = amt1
	s.release()
	print("depositing ended ")
def withdraw():
	print("withdrawing started")
	s.acquire()
	global balance
	amt2 = balance
	time.sleep(2)
	amt2 -= 100
	s.release()
	balance = amt2
	print("withdrawing ended ")

print("aate hi kam shuru kar diye", balance)
a = threading.Thread(target=deposit)
m = threading.Thread(target=withdraw)
a.start()
m.start()
a.join()
m.join()
print("har bar garam kar k chod dayta ho", balance)