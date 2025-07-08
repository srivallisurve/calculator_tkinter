from tkinter import*
window=Tk()
window.title("Calculator")
window.geometry("500x440")
window.configure(bg="pink")
window.resizable(False,False)
label=Label(window,text="Calculator",
            font=("Times New Roman",40,"bold"))
label.place(x=110,y=20,height=50,width=280)
data=''
def get_data(value):
    global data
    data=data+str(value)
    var.set(data)
    
def equal_data():
    global data
    total=str(eval(data))
    var.set(total)

def clear():
    global data
    data=""
    var.set(data)

var=StringVar()
txt=Entry(window,relief="sunken",font=("Times New Roman",20,"bold"),bd=3.5,
          textvariable=var)
txt.place(x=20,y=93,height=50,width=460)
bt1=Button(window,text="1",font=("Times New Roman",20,"bold"),
           command=lambda:get_data(1))
bt1.place(x=20,y=170,height=50,width=115)
bt2=Button(window,text="2",font=("Times New Roman",20,"bold"),
           command=lambda:get_data(2))
bt2.place(x=135,y=170,height=50,width=115)
bt3=Button(window,text="3",font=("Times New Roman",20,"bold"),
           command=lambda:get_data(3))
bt3.place(x=250,y=170,height=50,width=115)
bt_add=Button(window,text="+",font=("Times New Roman",20,"bold"),
           command=lambda:get_data("+"))
bt_add.place(x=365,y=170,height=50,width=115)

bt4=Button(window,text="4",font=("Times New Roman",20,"bold"),
           command=lambda:get_data(4))
bt4.place(x=20,y=220,height=50,width=115)
bt5=Button(window,text="5",font=("Times New Roman",20,"bold"),
           command=lambda:get_data(5))
bt5.place(x=135,y=220,height=50,width=115)
bt6=Button(window,text="6",font=("Times New Roman",20,"bold"),
           command=lambda:get_data(6))
bt6.place(x=250,y=220,height=50,width=115)
bt_sub=Button(window,text="-",font=("Times New Roman",20,"bold"),
           command=lambda:get_data("-"))
bt_sub.place(x=365,y=220,height=50,width=115)

bt7=Button(window,text="7",font=("Times New Roman",20,"bold"),
           command=lambda:get_data(7))
bt7.place(x=20,y=270,height=50,width=115)
bt8=Button(window,text="8",font=("Times New Roman",20,"bold"),
           command=lambda:get_data(8))
bt8.place(x=135,y=270,height=50,width=115)
bt9=Button(window,text="9",font=("Times New Roman",20,"bold"),
           command=lambda:get_data(9))
bt9.place(x=250,y=270,height=50,width=115)
bt_mul=Button(window,text="*",font=("Times New Roman",20,"bold"),
           command=lambda:get_data("*"))
bt_mul.place(x=365,y=270,height=50,width=115)

bt_dot=Button(window,text=".",font=("Times New Roman",20,"bold"),
           command=lambda:get_data("."))
bt_dot.place(x=20,y=320,height=50,width=115)
bt0=Button(window,text="0",font=("Times New Roman",20,"bold"),
           command=lambda:get_data(0))
bt0.place(x=135,y=320,height=50,width=115)
bt_clear=Button(window,text="C",font=("Times New Roman",20,"bold"),
           command=clear)
bt_clear.place(x=250,y=320,height=50,width=115)
bt_div=Button(window,text="/",font=("Times New Roman",20,"bold"))
bt_div.place(x=365,y=320,height=50,width=115)

bt_equal=Button(window,text="=",font=("Times New Roman",20,"bold"),
           command=equal_data)
bt_equal.place(x=95,y=370,height=50,width=300)

























window.mainloop()
