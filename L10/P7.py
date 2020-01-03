import threading
import time
def writing():
	print("writing started ")
	for  i in range(1,11):
		print("writing ", i ,"assignment")
		time.sleep(2)
	print("writing ended")
def music():
	print("Music started ")
	for i in range(1, 21):
		print("song " ,i , "played")
		time.sleep(1)
	print("Music stopped")
print("aate hi kam shuru kar diye")
a = threading.Thread(target=writing)
m = threading.Thread(target=music)
a.start()
m.start()
a.join()
m.join()
print("har bar garam kar k chod dayta ho")