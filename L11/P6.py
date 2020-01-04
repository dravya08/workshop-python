from tkinter import *

root = Tk()
root.title("Swagat")
root.geometry("500x500+500+500")

def f1():
	from tkinter import messagebox
	messagebox.showinfo("Welcome", "Aaya apka intazer tha")
def f2():
	import webbrowser
	webbrowser.open("www.instgram.com/dravya__gohil/")

btnClickMe = Button(root,text="Click me",font=("arial",18,"bold"),command=f1)
btnVisitMe = Button(root,text="VIsit me",font=("arial",18,"italic"),command=f2)
btnClickMe.pack(pady =10)
btnVisitMe.pack(pady =10)
root.mainloop()