from tkinter import *

root = Tk()
root.title("Color Me")
root.geometry("500x400+250+200")

def f1():
	root.configure(background=' darkred')

def f2():
	root.configure(background='green')

def f3():
	root.configure(background='blue')

btnRed = Button(root, text ="Red",font=("arial",18,"bold"),width = 10,command = f1)
btnGreen = Button(root, text ="Green",font=("arial",18,"bold"),width = 10,command = f2)
btnBlue = Button(root, text ="Blue",font=("arial",18,"bold"),width = 10,command = f3)

btnRed.pack(pady = 10)
btnGreen.pack(pady = 20)
btnBlue.pack(pady = 10)

root.mainloop()