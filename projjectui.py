import tkinter as t
import projectui2 as p2
import projectui3 as p3

win=t.Tk()
win.geometry('550x650')
win.title('Project Name')
win.configure(bg='white')
win.resizable(False,False)
def checkreview():
        p2.load()
def typereview():
        p3.load()
        
###########frames Design done###################
top=t.Frame(win,width=600,height=150,bd=2,relief='raise',pady=4,bg='white')
top.pack(side='top')
middle=t.Frame(win,width=600,height=150,bd=2,relief='raise',pady=30,bg='powderblue')
middle.pack(side='top')
bottom=t.Frame(win,width=600,height=150,bd=2,relief='raise',pady=20,padx=2,bg='yellow')
bottom.pack(side='bottom')
#############top Frame Design#####################
l1=t.Label(top,text='A Tale of Three Genres',font=('arial',18,'bold'),pady=12)
l1.pack(side='top')
con1='''This Application basically help the user to check the revies given by
any user on the websites or application is said to be bad or good
and it also gives a option to check the type of review that this
review basically belongs to which type we basically focus on
movie hotels and email data So Hurry Up and use it'''
l2=t.Label(top,text=con1,font=('arial',12),padx=20,justify='left',pady=12,bg='lightgreen')
l2.pack(side='top')
############middle frame design#######################
l3=t.Label(middle,text='Check The Review',font=('arial',16,'bold'),pady=10)
l3.pack(side='top')
con1='''  This section basically focus on the sentiment of the user acccording
  to the given feedback to use it please click on the given button '''
l4=t.Label(middle,text=con1,font=('arial',12),padx=20,justify='left',pady=12,bg='powderblue')
l4.pack(side='top')
b1=t.Button(middle,text='Check Review',font=('arial',16,'bold'),bg='powderblue',fg='red',command=checkreview)
b1.pack(side='top')
############bottom frame design#######################
l3=t.Label(bottom,text='Check Review Type',font=('arial',12,'bold'),pady=12)
l3.pack(side='top')
con1='''  This section basically focus on the type of review like which
  area this review is given like hotel movie or email to use it please
  click on the given button '''
l4=t.Label(bottom,text=con1,font=('arial',12),padx=20,justify='left',pady=12,bg='yellow')
l4.pack(side='top')
b1=t.Button(bottom,text='Check Review Type',font=('arial',12,'bold'),bg='powderblue',fg='red',command=typereview)
b1.pack(side='top')












