from tkinter import *
from login.uiloginuser import login
import mysql.connector
from tkinter import messagebox
import re
from user.datauser import saveUSER
""" Gui for user signup page"""


class uisingnup():
    def __init__(self):
        window = Tk()
        window.title("Taxi Booking")
        window.geometry("700x400")
        window.configure(bg='white')
        frame = Frame(window)
        frame.configure(bg="grey")
        frame.place(x=130, y=95)
        frame.configure(width=420, height=250)
        txtSignup = Label(window, text="SIGNUP", font=("comicsansm", 40, "bold"), bg="white", fg="black")
        txtSignup.place(x=250, y=1)
        user = Entry(window, width=20)
        user.place(x=350, y=100)
        mail = Entry(window, width=20)
        mail.place(x=350, y=130)
        password = Entry(window, width=20)
        password.place(x=350, y=160)
        phone = Entry(window, width=20)
        phone.place(x=350, y=190)
        lbluser = Label(window, text="USERNAME", bg="grey")
        lbluser.place(x=250, y=100)
        lblphone = Label(window, text="PHONE NO", bg="grey")
        lblphone.place(x=250, y=130)
        lblmail = Label(window, text="EMAIL", bg="grey")
        lblmail.place(x=250, y=160)
        lblpassw = Label(window, text="PASSWORD", bg="grey")
        lblpassw.place(x=250, y=190)
        member = Label(window, text="Already a Member?", bg='grey')
        member.place(x=250, y=270)

        def save():
            # Collecting data from the form
            name = user.get()
            phone_number = phone.get()
            email = mail.get()
            passwordd = password.get()

            # Connecting to the database
            conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='',
                                           database='taxi')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usersdata WHERE email=%s", (email,))
            results = cursor.fetchall()

            # Validating the form data
            if not name or not email or not password or not phone_number:
                messagebox.showerror("Invalid", "All fields are required")
            elif not re.match(r"[^@]", email):
                messagebox.showerror("Invalid", "Invalid email address")
            elif len(phone_number) > 10:
                messagebox.showerror("Invalid", "Mobile Number must be at least 10 characters")
            elif len(passwordd) < 8:
                messagebox.showerror("Invalid", "Password must be at least 8 characters")
            elif results:
                messagebox.showerror("Invalid", "Email already exists")
            else:
                print("Inserted Sucessfully!!")
                saveUSER(name,  phone_number, email,  password)
                messagebox.showinfo("Title", "User Registered")
                window.destroy()


        def forget(*args):
            login()
        loginLbl = Label(window, text="Login?", font=("Arial", 10, 'underline'), bg="grey")
        loginLbl.grid(column=0, row=1)  # For underline
        loginLbl.place(x=360, y=270)
        loginLbl.bind('<Button-1>', forget)




        savebtn=Button(window,text="Sign In",command=save,bg="black",fg="white")
        savebtn.place(x=350,y=230)





        window.mainloop()
