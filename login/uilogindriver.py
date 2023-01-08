from tkinter import *
from tkinter import messagebox
from tkinter import Checkbutton
from driver.driverprofile import driverprofile

import Global
from user.signup import Signup
from user.datauser import searchUSER
class driverlogin():
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
                        welcome()
        window = Tk()
        window.title("Login")
        window.geometry("700x400")
        window.configure(bg='#6C8A9B')

        txtLogin = Label(window,text="LOGIN  ",font= ("comicsansm",40,"bold"),bg="#6C8A9B",fg="#F9F5EF")
        txtLogin.place(x=250,y=1)
        mail = Entry (window,width=20)
        mail.place(x=350,y=100)
        password = Entry(window, width=20,show="*")
        password.place(x=350, y=150)
        lblgmail = Label(window,text="EMAIL",bg="#FD6574")
        lblgmail.place(x=250,y=100)
        lblpassword = Label(window, text="PASSWORD", bg="#FD6574")
        lblpassword.place(x=250, y=150)
        savebtn=Button(window,text="LogIn",bg="#FD6574", command=driverprofile)
        savebtn.place(x=350,y=200)

        passshow = Checkbutton(window,text="show password",command=show_password,bg="#6C8A9B")
        passshow.place(x=500,y=150)
        window.mainloop()