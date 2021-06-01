from tkinter import *
s=""
root = Tk()

def do1():
    global s 
    s = s + "1"
    show()
    
def do2():
    global s 
    s = s + "2"
    show()
    
def do3():
    global s 
    s = s + "3"
    show()
    
def do4():
    global s 
    s = s + "4"
    show()
    
def do5():
    global s 
    s = s + "5"
    show()
    
def do6():
    global s 
    s = s + "6"
    show()
    
def do7():
    global s 
    s = s + "7"
    show()
    
def do8():
    global s 
    s = s + "8"
    show()
    
def do9():
    global s 
    s = s + "9"
    show()
    
def do10():
    global s 
    s = s + "%"
    show()
    
def do11():
    global s 
    s = s + "+"
    show()
    
def do12():
    global s 
    s = s + "-"
    show()
    
def do13():
    global s 
    s = s + "*"
    show()
    
def do14():
    global s 
    s = s + "0"
    show()
    
def do15():
    global s 
    s = s + "/"
    show()
    
def eq():
    global s
    if "+" in s:
        a,b = map(float,s.split("+"))
        res = a+b
    if "-" in s:
        a,b = map(float,s.split("-"))
        res = a-b
    if "*" in s:
        a,b = map(float,s.split("*"))
        res = a*b
    if "/" in s:
        a,b = map(float,s.split("/"))
        res = a//b
    if "%" in s:
        a,b = map(float,s.split("%"))
        res = a%b
    s = s + "=" + str(res) 
    Label(root,text=s,bg="white",fg="black").grid(row=1,column=4)
    
def show():
    global s
    Label(root,text=s,bg="white",fg="black").grid(row=1,column=4)

def clr():
    global s
    s = "                          "
    show()
    s=""
    
Button(root,text="1",command=do1,fg="white",bg="red",height=3,width=4,bd=5).grid(row=2,column=1)
Button(root,text="2",command=do2,fg="white",bg="red",height=3,width=4,bd=5).grid(row=2,column=2)
Button(root,text="3",command=do3,fg="white",bg="red",height=3,width=4,bd=5).grid(row=2,column=3)
Button(root,text="4",command=do4,fg="white",bg="red",height=3,width=4,bd=5).grid(row=3,column=1)
Button(root,text="5",command=do5,fg="white",bg="red",height=3,width=4,bd=5).grid(row=3,column=2)
Button(root,text="6",command=do6,fg="white",bg="red",height=3,width=4,bd=5).grid(row=3,column=3)
Button(root,text="7",command=do7,fg="white",bg="red",height=3,width=4,bd=5).grid(row=4,column=1)
Button(root,text="8",command=do8,fg="white",bg="red",height=3,width=4,bd=5).grid(row=4,column=2)
Button(root,text="9",command=do9,fg="white",bg="red",height=3,width=4,bd=5).grid(row=4,column=3)
Button(root,text="%",command=do10,fg="white",bg="red",height=3,width=4,bd=5).grid(row=5,column=1)
Button(root,text="+",command=do11,fg="white",bg="red",height=3,width=4,bd=5).grid(row=5,column=2)
Button(root,text="-",command=do12,fg="white",bg="red",height=3,width=4,bd=5).grid(row=5,column=3)
Button(root,text="*",command=do13,fg="white",bg="red",height=3,width=4,bd=5).grid(row=6,column=1)
Button(root,text="0",command=do14,fg="white",bg="red",height=3,width=4,bd=5).grid(row=6,column=2)
Button(root,text="/",command=do15,fg="white",bg="red",height=3,width=4,bd=5).grid(row=6,column=3)
Button(root,text="=",command=eq,fg="white",bg="black",height=3,width=4,bd=5).grid(row=7,column=1)
Button(root,text="clear",command=clr,fg="white",bg="black",height=3,width=4,bd=5).grid(row=7,column=2)
Button(root,text="QUIT",command=root.destroy,fg="white",bg="black",height=3,width=4,bd=5).grid(row=7,column=3)

root.mainloop()