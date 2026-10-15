from tkinter import *
from tkinter import messagebox
import database
win=Tk()
win.geometry("600x300")
win.config(bg="#95c5e2")
win.title("Login form")

#function
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_email.delete(0,END)
    ent_password.delete(0,END)
    ent_fname.focus_set()
def sign_up():
    fname=ent_fname.get()
    lname = ent_lname.get()
    email= ent_email.get()
    password = ent_password.get()
    if not email or not password:
        messagebox.showerror('error','email and password are required')
        return
    database.sign_up(fname,lname,email,password)
    messagebox.showinfo("success","sign up successful")
    clear()

def sign_in():
    email=ent_email.get()
    password=ent_password.get()
    if not email and not password:
        messagebox.showerror("error","enter email and password")
        return
    login=database.sign_in(email,password)
    if login:
        messagebox.showinfo("success","welcome"+str(login[1])+"!")
    else:
        messagebox.showerror("error","email or password is incorrect")

#wedget
lbl_fname=Label(win,text="FRIST NAME:",font="arial 15 bold",width=10,bg="#95c5e2")
lbl_fname.place(x=70,y=12)

lbl_lname=Label(win,text="LAST NAME:",font="arial 15 bold",width=10,bg="#95c5e2")
lbl_lname.place(x=70,y=62)

lbl_EMAIL=Label(win,text="EMAIL:",font="arial 15 bold",width=10,bg="#95c5e2")
lbl_EMAIL.place(x=60,y=112)

lbl_star=Label(win,text="*",font="arial 15 bold",bg="#95c5e2",fg="red")
lbl_star.place(x=69,y=112)

lbl_password=Label(win,text="PASSWORD:",font="arial 15 bold",width=10,bg="#95c5e2")
lbl_password.place(x=69,y=162)

lbl_star1=Label(win,text="*",font="arial 15 bold",bg="#95c5e2",fg="red")
lbl_star1.place(x=50,y=162)


ent_fname=Entry(win,width=45)
ent_fname.place(x=200,y=13,height=25)

ent_lname=Entry(win,width=45)
ent_lname.place(x=200,y=63,height=25)

ent_email=Entry(win,width=45)
ent_email.place(x=200,y=113,height=25)


ent_password=Entry(win,width=45)
ent_password.place(x=200,y=163,height=25)


btn_up=Button(win,text="Sign up",font="arial 18 bold",width=10,command=sign_up)
btn_up.place(x=80,y=230)

btn_in=Button(win,text="Sign in",font="arial 18 bold",width=10,command=sign_in)
btn_in.place(x=380,y=230)



win.mainloop()