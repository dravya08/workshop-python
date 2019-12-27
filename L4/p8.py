'''
wapp to read a username & password
if username is kamal
& password is borivali
then o/p: Welcome
else o/p: try again


'''
import getpass
username = input("Enter username ")
password = getpass.getpass("Enter password ")

if((username =='kamal') and (password== 'borivali')):
	print("Welcome")
else:
	print("Try Again")

