from tkinter import *
from PIL import ImageTk
window=Tk()
window.geometry('1280x700+0+0')
window.resizable(False,False)
backgroundImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

#frame
loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150)

logoImage=PhotoImage(file='login.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameImage=PhotoImage(file='stu.png')
usernamelabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
usernamelabel.grid(row=1,column=0,padx=20,pady=10)

usernameEntry=Entry(loginFrame,font=('times new roman',20),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,padx=20,pady=10)

#password
passwordImage=PhotoImage(file='pwd.png')
passwordlabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
passwordlabel.grid(row=2,column=0,padx=20,pady=10)

passwordEntry=Entry(loginFrame,font=('times new roman',20),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,padx=20,pady=10)

loginButton=Button(loginFrame,text="Login",font=('time new roman',10,'bold'))
loginButton.grid(row=3,column=1)
window.mainloop()