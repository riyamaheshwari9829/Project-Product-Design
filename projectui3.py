import tkinter as t
from tkinter import ttk
import reviewtype as rt
from tkinter import messagebox
def load():
    def backendcode():
        text=t1.get("1.0", "end-1c")
        res=rt.predictdata([text])
        print('button clicked')
        if res[0]=='hotel':
            messagebox.showinfo("hotel","seems like it is a hotel review")
        elif res[0]=='movie':
            messagebox.showinfo("movie","seems like it is a movie review")
        elif res[0]=='mail':
            messagebox.showinfo("mail","seems like it is a mail review")    
    win=t.Tk()
    win.geometry('600x500')
    win.title('Project Name')
    win.resizable(False,False)
    ###########frames Design done###################
    top=t.Frame(win,width=600,height=100,bd=2,relief='raise',pady=4,padx=40)
    top.pack(side='top')
    middle=t.Frame(win,width=600,height=400,bd=2,relief='raise',pady=20,padx=20)
    middle.pack(side='top')
    ###########top frame design##########################
    l1=t.Label(top,text='Check Review Type',font=('arial',20,'bold'),pady=10)
    l1.pack(side='top')
    con1='''       This Section basically helps the user to guess the type of
        review it bassically take the data and accordingly predict
        that which type of review it belongs
        Try it Once'''
    l2=t.Label(top,text=con1,font=('arial',14),justify='left',pady=12)
    l2.pack(side='top')
    ########################middle part design###############
    l3=t.Label(middle,text='Fill Details',font=('arial',16,'bold'),justify='left')
    t1=t.Text(middle,height=8,width=45,font=('arial',11))
    b1=t.Button(middle,text='Submit',font=('arial',14),command=backendcode)
    l3.place(x=10,y=20)
    t1.place(x=10,y=70)
    b1.place(x=10,y=220)

