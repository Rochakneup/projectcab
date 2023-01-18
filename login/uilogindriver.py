from tkinter import *
from tkinter import messagebox
from tkinter import Checkbutton
from driver.driverprofile import driverprofile
from driver.signupdriver import Driversignup
from driver.databasedriver import searchDriver

import Global
"""Gui of driver login page"""
class driverlogin():
    # to hade the password
    def __init__(self):
        def show_password():
            if password.cget('show') == "*":
                password.config(show='')
            else:
                password.config(show='*')
        # validation
        def  logfun():
            drilog1 = Driversignup(dmail = mail.get(), dpassword= password.get())
            driver = searchDriver(drilog1)

            if driver != None:
                Global.driverAccount = driver
                messagebox.showinfo("Driver Login Sucessful", "Welcome {}".format(mail.get()))
                window.destroy()
                # window = Tk()
                driverprofile()
            else:
                messagebox.showerror("Title", "Incorrect username or password")
        #         gui of driveer login page
        window = Tk()
        window.title("Login")
        window.geometry("700x400")
        window.configure(bg='white')
        frame = Frame(window)
        frame.configure(bg="grey")
        frame.place(x=100, y=50)
        frame.configure(width=500, height=300)

        txtLogin = Label(window, text="LOGIN  ", font=("comicsansm", 30, "bold"), bg="grey", fg="black")
        txtLogin.place(x=300, y=50)
        mail = Entry(window, width=30, )
        mail.place(x=300, y=150, height=25)
        password = Entry(window, width=30, show="*")
        password.place(x=300, y=200, height=25)
        lblgmail = Label(window, text="EMAIL", font=("comicsansm", 20, "bold"), bg="grey")
        lblgmail.place(x=110, y=150)
        lblpassword = Label(window, text="PASSWORD", font=("comicsansm", 20, "bold"), bg="grey")
        lblpassword.place(x=110, y=200)
        savebtn = Button(window, text="LogIn", bg="black", command=logfun, fg="white")
        savebtn.place(x=300, y=270, width=150, height=50)

        passshow = Checkbutton(window, text="show password", command=show_password, font=("comicsansm", 10, "bold"),
                               bg="grey")
        passshow.place(x=400, y=240)
        window.mainloop()