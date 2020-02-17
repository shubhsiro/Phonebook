from tkinter import *
root=Tk()
Label(root,text="Project Title:PhoneBook",font='Arial 20').grid(row=0,column=0)
Label(root,text="Project of Python Database",font='Arial 15').grid(row=1,column=1)
Label(root,text="Developed By: Shubham Sirothiya",foreground="Blue",font='Arial 15').grid(row=2,column=1)
Label(root,text="---------------------",foreground="Blue",font='Arial 15').grid(row=3,column=1)
Label(root,text="make mouse movement over this screen to close",foreground="Red").grid(row=4,column=1)
def close(e=1):
    root.destroy()
root.bind('<Motion>',close)
root.mainloop()
