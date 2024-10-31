# import tkinter
# win=tkinter.Tk()
# win.title("Button")
# win.configure(bg='green')
# win.minsize(400,400)
# win.maxsize(600,600)

# btn1=tkinter.Button(win,text="button",bg='blue',fg='white',activebackground='blue',activeforeground='white',padx=10,pady=10)
# btn1.pack()
# win.mainloop()


# import tkinter
# win=tkinter.Tk()
# win.title("Button")
# win.configure(bg='red')
# win.minsize(400,400)
# win.maxsize(600,600)
# def submit():
#     print(e1.get())
#     l3.config(text=e1.get())

# l1=tkinter.Label(win,text="this the example of button submit")
# l1.place(x=100,y=30)

# l2=tkinter.Label(win,text="name",bg='red')
# l2.place(x=100,y=65)

# e1=tkinter.Entry(win)
# e1.place(x=150,y=65)
# btn1=tkinter.Button(win,text="button",bg='blue',fg='white',activebackground='blue',activeforeground='white',padx=10,pady=10,command=submit)
# # btn1.pack()
# btn1.place(x=300,y=200)
# l3=tkinter.Label(win)
# l3.place(x=150,y=250)
# win.mainloop()

# import tkinter
# win=tkinter.Tk()
# win.title("form")
# win.configure(bg='blue')
# win.minsize(400,400)
# win.maxsize(600,600)
# def submit():
#     print(e1.get())
#     # l3.config(text=e1.get())
#     f=open('tkinterlabel','a')
#     f.write(e1.get())

# l1=tkinter.Label(win,text="this the example of button submit")
# l1.place(x=100,y=30)

# l2=tkinter.Label(win,text="name",bg='blue')
# l2.place(x=100,y=65)

# e1=tkinter.Entry(win)
# e1.place(x=150,y=65)
# btn1=tkinter.Button(win,text="button",bg='red',fg='white',activebackground='red',activeforeground='white',padx=10,pady=10,command=submit)
# # btn1.pack()
# btn1.place(x=300,y=200)
# l3=tkinter.Label(win)
# l3.place(x=150,y=250)
# win.mainloop()

import tkinter
win=tkinter.Tk()
win.title("form")
win.configure(bg='blue')
win.minsize(400,400)
win.maxsize(600,600)
def submit():
    print(e1.get())
    # l3.config(text=e1.get())
    # f=open('tkinterlabel','a')
    # f.write(e1.get())
    if var.get()==1:
        print('Male')
    else:
        print('Female')

l1=tkinter.Label(win,text="this the example of button submit")
l1.place(x=100,y=30)

l2=tkinter.Label(win,text="name",bg='blue')
l2.place(x=100,y=65)

e1=tkinter.Entry(win)
e1.place(x=150,y=65)

l4=tkinter.Label(win,text='Gender',bg='blue')
l4.place(x=100,y=100)
var=tkinter.IntVar()
r1=tkinter.Radiobutton(win,text='Male',variable=var,value=1)
r1.place(x=150,y=100)
r2=tkinter.Radiobutton(win,text="Female",variable=var,value=2)
r2.place(x=230,y=100)

btn1=tkinter.Button(win,text="button",bg='red',fg='white',activebackground='red',activeforeground='white',padx=10,pady=10,command=submit)
# btn1.pack()
btn1.place(x=300,y=200)
l3=tkinter.Label(win)
l3.place(x=150,y=250)
win.mainloop()