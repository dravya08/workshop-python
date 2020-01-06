from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import *

def f1():
	root.withdraw()
	adst.deiconify()

def f2():
	adst.withdraw()
	root.deiconify()

def f4():
	vist.withdraw()
	root.deiconify()

def f3():
	stdata.delete(1.0,END)
	root.withdraw()
	vist.deiconify()
	con = None
	try:
		con = connect("system/abc123")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data =cursor.fetchall()
		msg = ""
		for d in data:
			msg = msg + "rno=" + str(d[0]) + "     name=" + str(d[1]) + "\n"
		stdata.insert(INSERT, msg)
	except DatabaseError as e:
		messagebox.showerror("Galat Kiya",e)
	finally:
		if con is not None:
			con.close()

def f5():
	con = None
	try:
		con = connect("system/abc123")
		rno = int(entAddRno.get())
		name = entAddName.get()
		cursor = con.cursor()
		sql = "insert into student values('%d','%s')"
		args =(rno , name)
		cursor.execute(sql % args)
		con.commit()
		msg = str(cursor.rowcount) + "records inserted"
		messagebox.showinfo("Sahi kiya", msg)
		entAddRno.delete(0,END)
		entAddName.delete(0,END)
		entAddRno.focus()
	except DatabaseError as e:
		con.rollback()
		print("issue ", e)
	finally:
		if con is not None:
			con.close()

root = Tk()
root.title("S.M.S")
root.geometry("500x500+300+100")

btnAdd = Button(root,text="Add",width =10,font =('arial',18,'bold'),command = f1)
btnView = Button(root,text="View",width =10,font =('arial',18,'bold'),command = f3)

btnAdd.pack(pady=10)
btnView.pack(pady=10)

adst = Toplevel(root)
adst.title("Add Student")
adst.geometry("500x500+300+100")
adst.withdraw()

lblAddRno = Label(adst,text="enter rno ",font =('arial',18,'bold'))
lblAddName = Label(adst,text="enter name ",font =('arial',18,'bold'))
entAddRno = Entry(adst,bd=5,font=('arial',18,'bold'))
entAddName = Entry(adst,bd=5,font=('arial',18,'bold'))
btnAddSave = Button(adst,text="Save",font =('arial',18,'bold'),command = f5)
btnAddBack = Button(adst,text="Back",font =('arial',18,'bold'),command = f2)

lblAddRno.pack(pady=5)
entAddRno.pack(pady=5)
lblAddName.pack(pady=5)
entAddName.pack(pady=5)
btnAddBack.pack(pady=5)
btnAddSave.pack(pady=5)

vist = Toplevel(root)
vist.title("View Student")
vist.geometry("500x500+300+100")
vist.withdraw()

stdata = scrolledtext.ScrolledText(vist,width=40, height=20)
btnViewBack = Button(vist,text="Back",font =('arial',18,'bold'),command = f4)

stdata.pack(pady=5)
btnViewBack.pack(pady=5)

root.mainloop()
























