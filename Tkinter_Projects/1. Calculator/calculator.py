from tkinter import *
from math import inf

root=Tk()

root.geometry("297x423")
root.maxsize(height=423,width=297)
root.minsize(height=423,width=297)
root.title("Simple Calculator")

root.iconphoto(False,PhotoImage(file='calculatoricon.ico'))

f_num=StringVar()
f_num.set("")

e=Entry(root,bg="white",fg="black",width=45,relief=SUNKEN,borderwidth=3)
e.grid(row=1,column=0,columnspan=4,pady=10,ipady=7)

display= Label(root,bg="white",fg="black",font=f"Arial 11",width=30,height=7,borderwidth=3,padx=10,wraplength=240,border=3)
display.grid(row=0,column=0,columnspan=4,pady=10)

#fun. defined here:

def buttonClick(number):
    current=e.get()
    e.delete(0,END)
    if current!="":
        if "." in current and number==".":
            number=0
    e.insert(0,current+str(number))

def backspace():
    current=e.get()
    e.delete(0,END)
    e.insert(0,current[0:-1])
    if current=="" and f_num.get()!="":
        f_num.set(f_num.get()[0:-1])
        display["text"]=f_num.get()

def clear():
    e.delete(0,END)
    f_num.set("")
    display["text"]="0"

def operatorCall(operator):
    current=e.get()
    if current=="" and f_num.get()=="":
        current="0"
    if current=="" and f_num.get()[-1] in ["+","-","*","/"]:
        current="0"
    e.delete(0,END)
    e.insert(0,current+str(operator))

    f_num.set(f_num.get() + e.get())
    display["text"]=f_num.get()
    
    e.delete(0,END)


def equal():
    current=e.get()
    e.delete(0,END)
    f_num.set(f_num.get() + current)
    try:
        ans=eval(f_num.get())
    except ZeroDivisionError:
        ans="inf"

    display["text"]=f"{f_num.get()}  =  {ans}"
    
    f_num.set(ans)
    e.delete(0,END)

#buttons here:
button_1= Button(root,text="1",fg="black",bg="#B9FFF8",activebackground="#A66CFF",activeforeground="white",padx=30,pady=10,command=lambda:buttonClick(1))
button_2= Button(root,text="2",fg="black",bg="#B9FFF8",activebackground="#A66CFF",activeforeground="white",padx=30,pady=10,command=lambda:buttonClick(2))
button_3= Button(root,text="3",fg="black",bg="#B9FFF8",activebackground="#A66CFF",activeforeground="white",padx=30,pady=10,command=lambda:buttonClick(3))
button_4= Button(root,text="4",fg="black",bg="#B9FFF8",activebackground="#A66CFF",activeforeground="white",padx=30,pady=10,command=lambda:buttonClick(4))
button_5= Button(root,text="5",fg="black",bg="#B9FFF8",activebackground="#A66CFF",activeforeground="white",padx=30,pady=10,command=lambda:buttonClick(5))
button_6= Button(root,text="6",fg="black",bg="#B9FFF8",activebackground="#A66CFF",activeforeground="white",padx=30,pady=10,command=lambda:buttonClick(6))
button_7= Button(root,text="7",fg="black",bg="#B9FFF8",activebackground="#A66CFF",activeforeground="white",padx=30,pady=10,command=lambda:buttonClick(7))
button_8= Button(root,text="8",fg="black",bg="#B9FFF8",activebackground="#A66CFF",activeforeground="white",padx=30,pady=10,command=lambda:buttonClick(8))
button_9= Button(root,text="9",fg="black",bg="#B9FFF8",activebackground="#A66CFF",activeforeground="white",padx=30,pady=10,command=lambda:buttonClick(9))
button_0= Button(root,text="0",fg="black",bg="#B9FFF8",activebackground="#A66CFF",activeforeground="white",padx=30,pady=10,command=lambda:buttonClick(0))

button_clear= Button(root,text="AC ",fg="black",bg="#FF4A4A",padx=60,pady=10,command=clear)
button_backspace= Button(root,text="<--",fg="black",bg="#6FEDD6",activebackground="#A66CFF",activeforeground="white",padx=24,pady=10,command=backspace)
button_add= Button(root,text="+",fg="black",bg="#6FEDD6",activebackground="#A66CFF",activeforeground="white",padx=28,pady=10,command=lambda:operatorCall("+"))
button_subs= Button(root,text="-",fg="black",bg="#6FEDD6",activebackground="#A66CFF",activeforeground="white",padx=30,pady=10,command=lambda:operatorCall("-"))
button_multi= Button(root,text="*",fg="black",bg="#6FEDD6",activebackground="#A66CFF",activeforeground="white",padx=30,pady=10,command=lambda:operatorCall("*"))
button_divide= Button(root,text="/",fg="black",bg="#6FEDD6",activebackground="#A66CFF",activeforeground="white",padx=30,pady=10,command=lambda:operatorCall("/"))
button_decimal= Button(root,text="Dec .",fg="black",bg="#B9FFF8",activebackground="#A66CFF",activeforeground="white",padx=20,pady=10,command=lambda:buttonClick("."))
button_equal= Button(root,text="=",fg="black",bg="#FF9551",padx=66.2,pady=10,command=equal)

button_1.grid(row=5,column=0)
button_2.grid(row=5,column=1)
button_3.grid(row=5,column=2)
button_4.grid(row=4,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=6,column=0)

button_equal.grid(row=6,column=2,columnspan=2)
button_add.grid(row=2,column=3)
button_subs.grid(row=4,column=3)
button_multi.grid(row=5,column=3)
button_divide.grid(row=3,column=3)
button_clear.grid(row=2,column=0,columnspan=2)
button_backspace.grid(row=2,column=2)
button_decimal.grid(row=6,column=1)

root.mainloop()
