import threading
import time
balance=500
s = threading.Semaphore()
def deposit():
	
	global  balance 
	s.acquire()
	amt1 = balance
	time.sleep(0.5)
	amt1 += 100
	balance = amt1
	s.release()
def withdraw():	
	global  balance 
	s.acquire()
	amt2 = balance
	time.sleep(0.5)
	amt2 -= 100
	balance = amt2
	s.release()
print("initial balance ",balance)
t1 = threading.Thread(target= deposit)
t2 = threading.Thread(target= withdraw)
t1.start()
t2.start()
t1.join()
t2.join()
print("final balance ",balance)
