import motion
from search import *
from tkinter import *
from tkinter import messagebox

import sqlite3
root=Tk()
root.geometry('500x500')
con=sqlite3.Connection('Contact.db')
cur=con.cursor()



def save():
    
    cur.execute("Create table if not exists contact_details (CID integer Primary Key autoincrement, fname varchar(20), mname varchar(20), lname varchar(20), company varchar(20), address varchar(30), city varchar(20), pin number, website_URL varchar(30), bdate date, pnumber number, email_ID varchar(30))")
    cur.execute("Insert into contact_details (fname, mname, lname, company, address, city, pin, website_URL, bdate, pnumber, email_ID) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get()))
    cur.execute("Select * from contact_details")
    con.commit()
    print(cur.fetchall())
    messagebox.showinfo("Save", "Record Successfully Saved")


a=PhotoImage(file='phone_icon_gif.gif')
Label(root,image=a).grid(row =0,column=0,columnspan=4)

##cont_id=Entry(root)

Label(root,text="First Name").grid(row=1,column=0)
e1=Entry(root)
e1.grid(row=1,column=1)

Label(root,text="Middle Name").grid(row=2,column=0)
e2=Entry(root)
e2.grid(row=2,column=1)

Label(root,text="Last Name").grid(row=3,column=0)
e3=Entry(root)
e3.grid(row=3,column=1)

Label(root,text="Company Name").grid(row=4,column=0)
e4=Entry(root)
e4.grid(row=4,column=1)

Label(root,text="Address").grid(row=5,column=0)
e5=Entry(root)
e5.grid(row=5,column=1)

Label(root,text="City").grid(row=6,column=0)
e6=Entry(root)
e6.grid(row=6,column=1)

Label(root,text="Pin Code").grid(row=7,column=0)
e7=Entry(root)
e7.grid(row=7,column=1)

Label(root,text="Website URL").grid(row=8,column=0)
e8=Entry(root)
e8.grid(row=8,column=1)

Label(root,text="Date of Birth").grid(row=9,column=0)
e9=Entry(root)
e9.grid(row=9,column=1)

v1=StringVar()
Label(root,text="Select Phone Type",font="Arial 15",foreground="Blue").grid(row=10,column=0)
r1=Radiobutton(root,text="Office",variable=v1,value='office').grid(row=10,column=1)
r2=Radiobutton(root,text="Home",variable=v1,value='Home').grid(row=10,column=2)
r3=Radiobutton(root,text="Mobile",variable=v1,value='Mobile').grid(row=10,column=3)

Label(root,text="Phone Number").grid(row=11,column=0)
e10=Entry(root)
e10.grid(row=11,column=1)

v2=StringVar()
Label(root,text="Select Email Type",font="Arial 15",foreground="Blue").grid(row=12,column=0)
Radiobutton(root,text="Office",variable=v2,value='Office').grid(row=12,column=1)
Radiobutton(root,text="Personal",variable=v2,value='Personal').grid(row=12,column=2)

Label(root,text="Email id").grid(row=13,column=0)
e11=Entry(root)
e11.grid(row=13,column=1)

    
def close():
    root.destroy()


def edit():
    root=Tk()
    root.geometry('500x500')
    Label(root,text="Do you want to Update or Delete",font='Arial 15',bg='Light Blue').grid(row=0,column=1)
    Label(root,text="Type 1 for update And 2 for Delete",font='Arial 15',bg='Light Blue').grid(row=1,column=1)
    p=Entry(root)
    p.grid(row=1,column=2)
    if(p.get()==1):
        Label(root,text="Which Contact ID do you want to update?").grid(row=2,column=1)
        u1=Entry(root)
        u1.grid(row=2,column=2)
        Label(root,text="Which column do you want to update?").grid(row=3,column=1)
        c1=Entry(root)
        c1.grid(row=3,column=2)
        Label(root,text="enter the text to be updated").grid(row=4,column=1)
        t1=Entry(root)
        t1.grid(row=4,column=2)
        if(c1.get()==1):
            cur.execute("update contact_details set fname = ?",(t1.get()))
            con.commit()
        elif(c1.get()==2):
            cur.execute("update contact_details set mname = ?",(t1.get()))
            con.commit()
        elif(c1.get()==3):
            cur.execute("update contact_details set lname = ?",(t1.get()))
            con.commit()
        elif(c1.get()==4):
            cur.execute("update contact_details set company = ?",(t1.get()))
            con.commit()
        elif(c1.get()==5):
            cur.execute("update contact_details set address = ?",(t1.get()))
            con.commit()
        elif(c1.get()==6):
            cur.execute("update contact_details set city = ?",(t1.get()))
            con.commit()
        elif(c1.get()==7):
            cur.execute("update contact_details set pin = ?",(t1.get()))
            con.commit()
        elif(c1.get()==8):
            cur.execute("update contact_details set website_URL = ?",(t1.get()))
            con.commit()
        elif(c1.get()==9):
            cur.execute("update contact_details set bdate = ?",(t1.get()))
            con.commit()
        elif(c1.get()==10):
            cur.execute("update contact_details set pnumber = ?",(t1.get()))
            con.commit()
        elif(c1.get()==11):
            cur.execute("update contact_details set email_ID = ?",(t1.get()))
            con.commit()
    elif(p.get()==2):
        Label(root,text="Which Contact ID do you want to Delete?").grid(row=2,column=1)
        u1=Entry(root)
        u1.grid(row=2,column=2)
        
        

    else:
        Label(root,text="Wrong Choice").grid(row=5,column=1)
    
    
Button(root,text="Save",command=save).grid(row=14,column=0)
Button(root,text="Search",command=search_func).grid(row=14,column=1)
Button(root,text="Close",command=close).grid(row=14,column=2)
Button(root,text="Edit",command=edit).grid(row=14,column=3)



root.mainloop()
