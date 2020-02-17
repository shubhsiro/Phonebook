from tkinter import *
import sqlite3
def search_func():
    root=Tk()
    root.geometry('500x500')
    
    Label(root,text="Searching Phone Book",bg='Light blue',font="Arial 20").grid(row=0,column=1)
    lb=Listbox(root)
    
    
    Label(root,text="Enter Name: ").grid(row=1,column=0)
    e=Entry(root)
    e.grid(row=1,column=1)
    
    def func(self=1):
        con=sqlite3.Connection('Contact.db')
        cur=con.cursor()
        
        a=e.get()
        cur.execute("Select fname,mname,lname from contact_details where fname LIKE ?",('%'+a+'%',))
        stor=cur.fetchall()
        lb.delete(0,END)
        for i in range(len(stor)):
            na=' '
            fname=stor[i][0]
            mname=stor[i][1]
            lname=stor[i][2]
            na=' '+fname+' '+mname+' '+lname
            lb.insert(END,na)

        def print_details(event):
            widget=event.widget
            selection=widget.curselection()
            value=widget.get(selection[0])
            shu=value.split
            cur.execute("Select * from contact_details where fname like ? or mname like ? or lname like ?",('%'+shu[0]+'%','%'+shu[1]+'%','%'+shu[2]+'%'))
            flag=cur.fetchall()
            fname='First Name:'+flag[0][1]
            mname='Middle Name:'+flag[0][3]
            lname='Last Name:'+flag[0][5]
            lb.delete(0,END)
            lb.insert(END,fname)
            lb.insert(END,mname)
            lb.insert(END,lname)
        lb.bind("<Double-Button-1>",print_details)
    lb.grid(row=3,column=1)
    
    
    func()
    root.bind("<KeyPress>",func)
    
    
    

    def close_search():
        root.destroy()
    Button(root,text="Close",command=close_search).grid(row=3,column=3)
    root.mainloop()

