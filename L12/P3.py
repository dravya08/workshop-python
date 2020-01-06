from tkinter import *

win = Tk()
win.title("Future Plans")
win.geometry("500x400+250+200")

def f1():
	res = s.get()
	selection = ''
	if res == 1:
		selection = "Job"
	elif res == 2:
		selection = "MS"
	elif res == 3:
		selection = "MBA"
	else:
		selection = "MTech"
	from tkinter import messagebox
	messagebox.showinfo("Selection", selection)

s = IntVar()
s.set(1)
rbJob = Radiobutton(win,text="Job",font=('arial',18,'bold'),variable=s, value=1).grid(sticky='W')
rbMs= Radiobutton(win,text="Ms",font=('arial',18,'bold'),variable=s, value=2).grid(sticky='W')
rbMba = Radiobutton(win,text="Mba",font=('arial',18,'bold'),variable=s, value=3).grid(sticky='W')
rbMtech = Radiobutton(win,text="Mtech",font=('arial',18,'bold'),variable=s, value=4).grid(sticky='W')
btnSubmit = Button(win,text="Submit",font=('arial',18,'bold'),command =f1).grid()

win.mainloop()


