from tkinter import *

win = Tk()
win.title("Sandwich")
win.geometry("500x400+250+200")

def f1():
	order =""
	if t.get() == 1:
		order += " Tomato "
	if o.get() == 1:
		order += " Onion "
	if p.get() == 1:
		order += " Potato "
	if c.get() == 1:
		order += " Cheese "
	from tkinter import messagebox
	if t.get()==0 and o.get()==0 and p.get()==0 and c.get()==0:
		messagebox.showerror("Error","Kuch tho order kar")
	else:
		messagebox.showinfo("order", order)

lblSeletionOption = Label(win,text="Select Option",font =('arial',18,'bold')).grid()

t,o,p,c = IntVar(),IntVar(),IntVar(),IntVar()
rbTomato = Checkbutton(win,text="Tomato",font=('arial',18,'bold'),variable = t).grid(sticky='W')
rbOnion= Checkbutton(win,text="Onion",font=('arial',18,'bold'),variable = o).grid(sticky='W')
rbPotato = Checkbutton(win,text="Potato",font=('arial',18,'bold'),variable = p).grid(sticky='W')
rbCheese = Checkbutton(win,text="Cheese",font=('arial',18,'bold'),variable = c).grid(sticky='W')
btnOrder = Button(win,text="Order",font=('arial',18,'bold'),command = f1).grid()

win.mainloop()


