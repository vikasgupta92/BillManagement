from tkinter import *
root=Tk()
root.title("calculator")
root.geometry("380x550+200+100")

#---lambda fun ---
def enterNumber(x):
    if entry_box.get()=='0':
        entry_box.delete(0,'end')
        entry_box.insert(0,str(x))
    else:
        length=len(entry_box.get())
        entry_box.insert(length,str(x))
#enter op in entry box
def enter_operator(x):
        if(entry_box.get()!='0'):
            length=len(entry_box.get())
            entry_box.insert(length,btn_operator[x]['text'])


def funclear():
    entry_box.delete(0,END)
    entry_box.insert(0,'0')

            #Last stmtss
#-------entry Box----------
entry_box=Entry(font='verdana 14',width=24,bd=6,justify=RIGHT)
entry_box.insert(0,'0')
entry_box.place(x=30,y=10)

#using lambda
btn_numbers=[]
for i in range(10):
    btn_numbers.append(Button(width=4,text=str(i),bd=6,command=lambda x=i:enterNumber(x)))
#btn positions
btn_txt=1
for i in range(0,3):
    for j in range(0,3):
        btn_numbers[btn_txt].place(x=30+j*90,y=70+i*70)
        btn_txt+=1

btn_zero=Button(width=14,text='0',bd=5,command=lambda x=0:enterNumber(x))
btn_zero.place(x=25,y=280)

#bt_clear=Button(width=4,text='c',font='times 15 bold', bd=5,commnad=funclear)
#----button operator--------
btn_operator=[]
for i in range(4):
    btn_operator.append(Button(width=3, font='times 11 bold',bd=5,command=lambda x=i:enter_operator(x)))
btn_operator[0]['text']='+'
btn_operator[1]['text']='-'
btn_operator[2]['text']='*'
btn_operator[3]['text']='/'
for i in range(4):
    btn_operator[i].place(x=290,y=70+i*70)

bt_clear=Button(width=4,text='c',font='times 15 bold', bd=5,commnad=funclear)
btn_clear(x=25,y=280)
root.mainloop()