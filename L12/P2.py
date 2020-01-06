from tkinter import *

root = Tk()
root.title("Color Me 2")
root.geometry("500x400+250+200")

def f1(num):
	if num==1:
		root.configure(background='red')
	elif num==2:
		root.configure(background='green')
	else:
		root.configure(background='blue')

btnRed = Button(root, text ="Red",font=("arial",18,"bold"),width = 5,command =lambda:f1(1))
btnGreen = Button(root, text ="Green",font=("arial",18,"bold"),width = 5,command =lambda:f1(2))
btnBlue = Button(root, text ="Blue",font=("arial",18,"bold"),width = 5,command =lambda:f1(3))

btnRed.place(x = 10, y = 50)
btnGreen.place(x = 150, y = 50)
btnBlue.place(x = 300 , y = 50)

root.mainloop()