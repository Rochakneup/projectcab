from tkinter import *
from tkinter import Checkbutton
from PIL import ImageTk,Image
from tkinter import messagebox
import Global
from user.signup import Signup
from user.datauser import searchUSER
from welcome.welcomeui import windowTrip
import tkinter as tk
class login():
    def __init__(self):
        def show_password():
            if password.cget('show') == "*":
                password.config(show='')
            else:
                password.config(show='*')

        def logfun():
            cuslog1 = Signup(cmail=mail.get(), cpassword=password.get())
            customer = searchUSER(cuslog1)

            if customer != None:
                Global.customerAccount = customer
                messagebox.showinfo("Customer Login Sucessful", "Welcome {}".format(mail.get()))
                window.destroy()
                # window = Tk()
                from welcome.welcomeui import windowTrip
                windowTrip()

            else:
                messagebox.showerror("Title", "Incorrect username or password")



        window = Tk()
        window.title("Login")
        window.geometry("700x400")
        window.configure(bg='white')
        tmpImage = Image.open('login1.jpg')
        imgFile = ImageTk.PhotoImage(tmpImage)
        imgFile_lbl = Label(window, image=imgFile)
        imgFile_lbl.image = imgFile
        imgFile_lbl.place(x=1, y=1)
        frame = Frame(window)
        frame.configure(bg="grey")
        frame.place(x=100, y=50)
        frame.configure(width=500, height=300)



        txtLogin = Label(window,text="LOGIN  ",font= ("comicsansm",30,"bold"),bg="grey",fg="black")
        txtLogin.place(x=300,y=50)
        mail = Entry (window,width=30,)
        mail.place(x=300,y=150,height=25)
        password = Entry(window, width=30,show="*")
        password.place(x=300, y=200,height=25)
        lblgmail = Label(window,text="EMAIL",font= ("comicsansm",20,"bold") ,bg="grey")
        lblgmail.place(x=110,y=150)
        lblpassword = Label(window, text="PASSWORD",font= ("comicsansm",20,"bold"), bg="grey")
        lblpassword.place(x=110, y=200)
        savebtn=Button(window,text="LogIn",bg="black", command=logfun,fg="white")
        savebtn.place(x=300,y=270,width=150,height=50)

        passshow = Checkbutton(window,text="show password",command=show_password,font= ("comicsansm",10,"bold"), bg="grey")
        passshow.place(x=400,y=240)










        window.mainloop()
