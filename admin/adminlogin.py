from tkinter import *
import Global
from tkinter import messagebox
from admin.adminprofile import profile
class adminui():
    def __init__(self):
        window = Tk()
        window.title("Taxi Booking")
        window.geometry("700x400")

        def show_password():
            if password.cget('show') == "*":
                password.config(show='')
            else:
                password.config(show='*')

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
        savebtn = Button(window, text="LogIn", bg="black", command=profile, fg="white")
        savebtn.place(x=300, y=270, width=150, height=50)

        passshow = Checkbutton(window, text="show password", command=show_password, font=("comicsansm", 10, "bold"),
                               bg="grey")
        passshow.place(x=400, y=240)