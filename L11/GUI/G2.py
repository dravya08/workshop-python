from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Even Odd circle")
root.geometry("400x300+350+270")
def f1():
	try:	
		s1 = entNumber.get()
		n1 = int(s1)
		msg = ""
		if n1 % 2 == 0:
			msg = "even"
		else:
			msg = "odd"
		messagebox.showinfo("jawab",msg)
	except ValueError:
		messagebox.showerror("galat kiya",'u need to enter integers only')
		entNumber.delete(0,END)
		entNumber.focus()

lblNumber = Label(root,text="enter number",font=("arial",18,"bold"))
entNumber = Entry(root,bd=5,font=("arial",18,"bold"))
btnfind = Button(root,text="Find",font=("arial",18,"bold"),command=f1)
lblNumber.pack(pady=10)
entNumber.pack(pady=20)
btnfind.pack(pady=30)
root.mainloop()
