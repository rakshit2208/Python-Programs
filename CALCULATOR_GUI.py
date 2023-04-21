from tkinter import *
root=Tk()
root.title("MY CALCULATOR")
root.geometry("450x900")
root.configure(background="indigo")
def click(event):
    global scvalue
    text = event.widget.cget("text")
    #print(text)
    if text == "=" :
       if scvalue.get().isdigit():
           value = int(scvalue.get())
       else:
            try:
               value = eval(scvalue.get())
            except Exception as e:
               print(e)
               value="Error"

       scvalue.set(value)
       try:
          screen.update()
       except:
          pass
    elif text=="c":
       scvalue.set("")
       try:
          screen.update()
       except:
          pass
    else:
       scvalue.set(scvalue.get()+ text)
       try:
          screen.update()
       except:
          pass
       

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="sans-sarif 20 bold",bg="skyblue",fg="red",relief=SUNKEN).pack(fill=X,ipadx=10,padx=10,pady=10)

f=Frame(root,bg="lavender")
b=Button(f,text="9",padx=28,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="8",padx=28,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="7",padx=28,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="pink")
b=Button(f,text="6",padx=28,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="5",padx=28,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="4",padx=28,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="lavender")
b=Button(f,text="3",padx=28,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="2",padx=28,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="1",padx=28,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="pink")
b=Button(f,text="0",padx=28,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=20,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="-",padx=28,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=20,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="*",padx=28,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=20,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="lavender")
b=Button(f,text="/",padx=30,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="%",padx=26,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="=",padx=28,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="pink")
b=Button(f,text="c",padx=28,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=14,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="+",padx=34,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=14,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="Off",padx=22,pady=18,font="sans-sarif 20 bold")
b.pack(side=LEFT,padx=14,pady=5)
b.bind("<Button-1>",quit)
f.pack()

root.mainloop()