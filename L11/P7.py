from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Even Odd Calci ")
root.geometry("400x300+500+400")
def f1():
    try:
        s1= entNumber.get()
        n1 = int(s1)
        msg = ""
        if n1 % 2 == 0:
            msg = "Even"
        else:
            msg ="Odd"
        messagebox.showinfo("Jawab", msg)
    except ValueError:
        messagebox.showerror("Galat Kiya", 'u need to enter interger only')
        entNumber.delete(0,END)
        entNumber.focus()

lblNumber = Label(root,text ="enter number", font=("arial", 18 ,"bold"))
entNumber = Entry(root,bd = 5, font=("arial", 18 ,"bold"))
btnFind = Button(root,text ="FInd", font=("arial", 18 ,"bold"),command=f1)
lblNumber.pack(pady = 10)
entNumber.pack(pady = 20)
btnFind.pack(pady =10)
root.mainloop()