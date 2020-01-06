from tkinter import * 
from tkinter import messagebox

win = Tk()
win.title("Kamal Classes")
win.geometry("300x500+200+100")
win.configure(background='powder blue')

def f1():
	fb,mat ="",""
	if s1.get() == 1:
		fb = "Fantastic"
	if s1.get() == 2:
		fb  = "Excellent"
	else:
		fb = "Superb"

	if n.get()==1:
		mat += "Notes"
	if s.get()==1:
		mat += "Software"
	if c.get()==1:
		mat += "Certificate"
	msg ="FeedBack" + fb + "\n" + "Materials" + mat
	messagebox.showinfo("Result", msg)

	to = "noron1999@gmail.com"
	subject="Feedback+Materials by Dravya Gohil"
	text = msg
	import smtplib
	sender = 'dravyagohil@gmail.com'
	password = '8108214452'
	message = 'Subject:{}\n\n{}'.format(subject,text) 
	server = smtplib.SMTP_SSL('smtp.gmail.com',465)
	server.ehlo()
	server.login(sender,password)
	print("logged in")
	try:
		server.sendmail(sender,to,message)
		print("enter email")
	except:
		print("Error sending email")
	server.quit

s1 = IntVar()
s1.set(1)

fb= Label(win,text="FeedBack",font=('arial',20,'bold')).grid(stick='w')
rbFantastic = Radiobutton(win,text="Fantastic",font=('arial',15,'bold'),variable=s1, value=1).grid(stick='w')
rbExcellent = Radiobutton(win,text="Excellent",font=('arial',15,'bold'),variable=s1, value=2).grid(stick='w')
rbSuperb = Radiobutton(win,text="Superb",font=('arial',15,'bold'),variable=s1, value=3).grid(stick='w')

n,s,c = IntVar(),IntVar(),IntVar()
lblMaterials = Label(win,text="Materials",font=('arial',20,'bold')).grid(sticky='w')
cbNotes = Checkbutton(win,text="Notes",font=('arial',15,'bold')).grid(sticky ='w')
cbSoftware = Checkbutton(win,text="Software",font=('arial',15,'bold')).grid(sticky ='w')
cbCertificate = Checkbutton(win,text="Certificate",font=('arial',15,'bold')).grid(sticky ='w')

BEmail = Button(win,text="Email",font=('arial',18,'bold'),command =f1).grid()







win.mainloop()