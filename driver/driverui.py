from tkinter import *

from login.uilogindriver import driverlogin
from tkinter import messagebox
import mysql.connector
import re
from driver.databasedriver import saveDRIVER
"""driver GUI for signup """
class driverui():
    def __init__(self):
        window = Tk()
        window.title("Taxi Booking")
        window.geometry("700x400")
        window.configure(bg='white')
        frame = Frame(window)
        frame.configure(bg="grey")
        frame.place(x=130, y=95)
        frame.configure(width=420, height=250)

        txtSignup = Label(window,text="SIGNUP",font= ("comicsansm",40,"bold"),bg="white",fg="black")
        txtSignup.place(x=250,y=1)
        user = Entry(window, width=20)
        user.place(x=350, y=100)
        mail = Entry(window, width=20)
        mail.place(x=350, y=130)
        password = Entry(window, width=20)
        password.place(x=350, y=160)
        phone = Entry(window, width=20)
        phone.place(x=350, y=190)
        lbldriver = Label(window, text="DRIVERNAME", bg="grey")
        lbldriver.place(x=250, y=100)
        lblphone = Label(window, text="PHONE NO", bg="grey")
        lblphone.place(x=250, y=130)
        lblmail = Label(window, text="EMAIL", bg="grey")
        lblmail.place(x=250, y=160)
        lblpassw = Label(window, text="PASSWORD", bg="grey")
        lblpassw.place(x=250, y=190)

        liscense = Entry(window, width=20)
        liscense.place(x=350, y=220)
        lblliscense = Label(window, text="LISCENSE NO", bg="grey")
        lblliscense.place(x=250, y=220)
        member= Label(window,text="Already a Member?",bg='grey')
        member.place(x=250,y=300)
        def forget(*args):
            driverlogin()
        loginLbl = Label(window, text="Login?", font=("Arial", 10, 'underline'), bg="grey")
        loginLbl.grid(column=0, row=1)  # For underline
        loginLbl.place(x=360, y=300)
        loginLbl.bind('<Button-1>', forget)
        # to ge data from database
        def save():
            name = user.get()
            phone_number = phone.get()
            email = mail.get()

            passwordd = password.get()


            conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='',
                                           database='taxi')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM drivers WHERE mail=%s", (email,))
            results = cursor.fetchall()

            if not name or not email or not password or not  phone_number or not liscense:
                messagebox.showerror("Invalid", "All fields are required")
            elif not re.match(r"[^@]+", email):
                messagebox.showerror("Invalid", "Invalid email address")
            elif len(phone_number) > 10:
                messagebox.showerror("Invalid", "Mobile Number must be at least 10 characters")
            elif len(passwordd) < 8:
                messagebox.showerror("Invalid", "Password must be at least 8 characters")
            elif results:
                messagebox.showerror("Invalid", "Email already exists")
            elif (liscense) > 10:
                messagebox.showerror("Invalid", "License not match")
            else:
                print("Inserted Sucessfully!!")
                saveDRIVER(name,  phone_number, email,  password)
                messagebox.showinfo("Title", "User Registered")
                window.destroy()



        savebtn=Button(window,text="Sign In",command=save,bg="black",fg="white")
        savebtn.place(x=350,y=260)

        window.mainloop()