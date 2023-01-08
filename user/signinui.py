from tkinter import *
from datauser import saveUSER
from login.uiloginuser import login
class uisingnup():
    def __init__(self):
        window = Tk()
        window.title("Taxi Booking")
        window.geometry("700x400")
        window.configure(bg='#6C8A9B')

        txtSignup = Label(window, text="SIGNUP", font=("comicsansm", 40, "bold"), bg="#6C8A9B", fg="#F9F5EF")
        txtSignup.place(x=250, y=1)
        user = Entry(window, width=20)
        user.place(x=350, y=100)
        mail = Entry(window, width=20)
        mail.place(x=350, y=130)
        password = Entry(window, width=20)
        password.place(x=350, y=160)
        phone = Entry(window, width=20)
        phone.place(x=350, y=190)
        lbluser = Label(window, text="USERNAME", bg="#FD6574")
        lbluser.place(x=250, y=100)
        lblphone = Label(window, text="PHONE NO", bg="#FD6574")
        lblphone.place(x=250, y=130)
        lblmail = Label(window, text="EMAIL", bg="#FD6574")
        lblmail.place(x=250, y=160)
        lblpassw = Label(window, text="PASSWORD", bg="#FD6574")
        lblpassw.place(x=250, y=190)
        member = Label(window, text="Already a Member?", bg='#6C8A9B')
        member.place(x=250, y=270)


        def forget(*args):
            login()
        loginLbl = Label(window, text="Login?", font=("Arial", 10, 'underline'), bg="#6C8A9B")
        loginLbl.grid(column=0, row=1)  # For underline
        loginLbl.place(x=360, y=270)
        loginLbl.bind('<Button-1>', forget)




        def save():
            # reading value from entry and send to library/middleware
            cname = (user.get())
            cmail = (mail.get())
            cpassword = (password.get())
            cphone = (phone.get())

            result = saveUSER(cname, cmail, cpassword,cphone)
            if (result == True):
                print("Error to insert")
            else:
                print("Insert Sucessfully")
        savebtn=Button(window,text="Sign In",command=save,bg="#FD6574")
        savebtn.place(x=350,y=230)


        window.mainloop()
