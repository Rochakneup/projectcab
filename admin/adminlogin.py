from tkinter import *
import Global
from tkinter import messagebox
from admin.adminprofile import profile
from admin.admingetset import adminsignup
from admin.admindatabase import searchAdmin
# gui for admin login
class adminui():
    def __init__(self):
        window = Tk()
        window.title("Taxi Booking")
        window.geometry("700x400")
        # code to hid epassword
        def show_password():
            if password.cget('show') == "*":
                password.config(show='')
            else:
                password.config(show='*')
        #         validation
        def logfun():
            cuslog1 = adminsignup(amail=mail.get(), apassword=password.get())
            customer = searchAdmin(cuslog1)

            if customer != None:
                Global.customerAccount = customer
                messagebox.showinfo("Customer Login Sucessful", "Welcome {}".format(mail.get()))
                window.destroy()
                # window = Tk()
                from welcome.welcomeui import windowTrip
                profile()

            else:
                messagebox.showerror("Title", "Incorrect username or password")
        # gui for login for admin
        window.configure(bg='white')
        frame = Frame(window)
        frame.configure(bg="grey")
        frame.place(x=100, y=50)
        frame.configure(width=500, height=300)
        # lable for login
        txtLogin = Label(window, text="LOGIN  ", font=("comicsansm", 30, "bold"), bg="grey", fg="black")
        txtLogin.place(x=300, y=50)
        # entry for email
        mail = Entry(window, width=30, )
        mail.place(x=300, y=150, height=25)
        # entry for password
        password = Entry(window, width=30, show="*")
        password.place(x=300, y=200, height=25)
        ## label for email
        lblgmail = Label(window, text="EMAIL", font=("comicsansm", 20, "bold"), bg="grey")
        lblgmail.place(x=110, y=150)
        # label for password
        lblpassword = Label(window, text="PASSWORD", font=("comicsansm", 20, "bold"), bg="grey")
        lblpassword.place(x=110, y=200)
        # button for login
        savebtn = Button(window, text="LogIn", bg="black", command=lambda :[logfun(), window.destroy()], fg="white")
        savebtn.place(x=300, y=270, width=150, height=50)
        # button which hides and shows password
        passshow = Checkbutton(window, text="show password", command=show_password, font=("comicsansm", 10, "bold"),
                               bg="grey")
        passshow.place(x=400, y=240)