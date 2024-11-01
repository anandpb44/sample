import tkinter
import mysql.connector

fom=tkinter.Tk()
fom.title("Form")
fom.configure(bg='white')
fom.minsize(400,400)
fom.maxsize(600,600)

def submit():
    g=''
    if var.get()==1:
        g='Male'
        print('Male')
    else:
        g='Female'
        print("Female")
    con=mysql.connector.connect(host='localhost',user='admin',password='admin123',database='form')
    con.autocommit=True
    cr=con.cursor()
    cr.execute("insert into details(id,name,age,gender)values(%s,%s,%s,%s)",(t1.get(),t2.get(),t3.get(),g))

l1=tkinter.Label(fom,text='id')
l1.place(x=90,y=80)
t1=tkinter.Entry(fom)
t1.place(x=140,y=80)

l2=tkinter.Label(fom,text='Name')
l2.place(x=90,y=120)
t2=tkinter.Entry(fom)
t2.place(x=140,y=120)

l3=tkinter.Label(fom,text='Age')
l3.place(x=90,y=160)
t3=tkinter.Entry(fom)
t3.place(x=140,y=160)

l4=tkinter.Label(fom,text='Gender')
l4.place(x=90,y=200)
var=tkinter.IntVar()
e1=tkinter.Radiobutton(fom,text='Male',variable=var,value=1)
e1.place(x=160,y=200)
e2=tkinter.Radiobutton(fom,text='Female',variable=var,value=2)
e2.place(x=240,y=200)

btn=tkinter.Button(fom,text='Submit',command=submit)
btn.place(x=150,y=250)
fom.mainloop()