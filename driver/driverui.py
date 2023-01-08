from tkinter import *
from driver.databasedriver import saveDRIVER
from login.uilogindriver import driverlogin
class driverui():
    def __init__(self):
        window = Tk()
        window.title("Taxi Booking")
        window.geometry("700x400")
        window.configure(bg='#6C8A9B')


        txtSignup = Label(window,text="SIGNUP",font= ("comicsansm",40,"bold"),bg="#6C8A9B",fg="#F9F5EF")
        txtSignup.place(x=250,y=1)
        user = Entry(window, width=20)
        user.place(x=350, y=100)
        mail = Entry(window, width=20)
        mail.place(x=350, y=130)
        password = Entry(window, width=20)
        password.place(x=350, y=160)
        phone = Entry(window, width=20)
        phone.place(x=350, y=190)
        lbldriver = Label(window, text="DRIVERNAME", bg="#FD6574")
        lbldriver.place(x=250, y=100)
        lblphone = Label(window, text="PHONE NO", bg="#FD6574")
        lblphone.place(x=250, y=130)
        lblmail = Label(window, text="EMAIL", bg="#FD6574")
        lblmail.place(x=250, y=160)
        lblpassw = Label(window, text="PASSWORD", bg="#FD6574")
        lblpassw.place(x=250, y=190)

        liscense = Entry(window, width=20)
        liscense.place(x=350, y=220)
        lblliscense = Label(window, text="LISCENSE NO", bg="#FD6574")
        lblliscense.place(x=250, y=220)
        member= Label(window,text="Already a Member?",bg='#6C8A9B')
        member.place(x=250,y=300)
        def forget(*args):
            driverlogin()
        loginLbl = Label(window, text="Login?", font=("Arial", 10, 'underline'), bg="#6C8A9B")
        loginLbl.grid(column=0, row=1)  # For underline
        loginLbl.place(x=360, y=300)
        loginLbl.bind('<Button-1>', forget)


        def save():
            # reading value from entry and send to library/middleware
            dname = (user.get())
            dmail = (mail.get())
            dpassword = (password.get())
            dphone = (phone.get())
            dliscenseno = (liscense.get())

            result = saveDRIVER(dname,dmail, dpassword,dphone,dliscenseno)
            if (result == True):
                print("Error to insert")
            else:
                print("driver added!")
        savebtn=Button(window,text="Sign In",command=save,bg="#FD6574")
        savebtn.place(x=350,y=260)

        window.mainloop()