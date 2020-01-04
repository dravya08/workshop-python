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
            me