from tkinter import *
import Global
from tkinter import messagebox
from admin.adminprofile import profile
class adminui():
    def __init__(self):
        window = Tk()
        window.title("Taxi Booking")
        window.geometry("700x400")
        window.configure(bg='#6C8A9B')
        def show_password():
            if password.cget('show') == "*":
                password.config(show='')
            else:
                password.config(show='*')

        # def logfun():
        #     cuslog1 = Signup(cmail=mail.get(), cpassword=password.get())
        #     customer = searchUSER(cuslog1)
        #
        #     if customer != None:
        #         Global.customerAccount = customer
        #         messagebox.showinfo("Customer Login Sucessful", "Welcome {}".format(mail.get()))
        #         window.destroy()
        #         # window = Tk()
        #         adminprofile()
        mail = Entry(window, width=20)
        mail.place(x=350, y=100)
        password = Entry(window, width=20, show="*")
        password.place(x=350, y=150)
        lblgmail = Label(window, text="EMAIL", bg="#FD6574")
        lblgmail.place(x=250, y=100)
        lblpassword = Label(window, text="PASSWORD", bg="#FD6574")
        lblpassword.place(x=250, y=150)
        savebtn = Button(window, text="LogIn", bg="#FD6574", command=profile)
        savebtn.place(x=350, y=200)

        passshow = Checkbutton(window, text="show password", command=show_password, bg="#6C8A9B")
        passshow.place(x=500, y=150)