# Importing Tkinter module
from tkinter import *
from PIL import ImageTk, Image
# Importing module created by me
from login.uiloginuser import login
from login.uilogindriver import driverlogin
from admin.adminlogin import adminui




""" Gui for main page"""

class first():
    def __init__(self):
        # Creating instance of Tk class
        window = Tk()

        # Setting the geometry of the window
        window.geometry("700x400")

        # Setting the title of the window
        window.title("Taxi Booking")

        # Setting the background color of the window
        window.configure(bg='#6C8A9B')

        # Adding image to the window
        myImg = ImageTk.PhotoImage(Image.open("taxi1.jpg"))
        mylabel = Label(image=myImg)
        mylabel.pack()



        # Adding a label with "CAB_MANDU" text
        taxitxt = Label(window,text="CAB_MANDU",font= ("comicsansm",35,"bold"),fg="black")
        taxitxt.place(x=1,y=0,width=700)

        # Adding a label for the driver
        txtDriver = Label(window,text=""" DRIVER """,font= ("comicsansm",15,"bold"),bg="black",fg="#F9F5EF")
        txtDriver.place(x=10,y=180)

        # function to go to driver signup page
        def gotosignindriver():
            # destroy the current window
            window.destroy()
            # import driver signup page
            from driver.driverui import driverui
            driverui.__init__(self=window)

        # function to go to user signup page
        def gotosigninuser():
            # destroy the current window
            window.destroy()
            # import user signup page
            from user.signinui import uisingnup
            uisingnup.__init__(self=window)

        # button to go to driver signup page
        btnSignupd = Button(window, text="Signup",bg="white",command=gotosignindriver)
        btnSignupd.place(x=10, y=225)

        # label for user section
        txtUser = Label(window,text=""" FIND A RIDE """,font= ("comicsansm",15,"bold"),bg="black",fg="#F9F5EF")
        txtUser.place(x=300,y=180)
        # button to go to user signup page
        btnSignupc = Button(window, text="Signup",bg="white", command=gotosigninuser)
        btnSignupc.place(x=300, y=225)

        # button for driver login
        btndLogin = Button(window, text="Login",bg="white",command=lambda :[window.destroy(),driverlogin()])
        btndLogin.place(x=80, y=225)

        # button for user login
        btnLogin = Button(window, text="Login",bg="white",command=lambda :[window.destroy(),login()])
        btnLogin.place(x=380, y=225)

        # label for admin section
        txtAdmin = Label(window,text=""" ADMIN """,font= ("comicsansm",15,"bold"),bg="black",fg="#F9F5EF")
        txtAdmin.place(x=600,y=180)
        # button for admin login
        btnloginad = Button(window, text="Login",bg="white", command=lambda :[window.destroy(),adminui()])
        btnloginad.place(x=625, y=225)












        window.mainloop()
first()