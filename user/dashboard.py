from tkinter import *
from PIL import ImageTk, Image
from login.uiloginuser import login
from driver.driverprofile import driverprofile
from login.uilogindriver import driverlogin
from admin.adminlogin import adminui


# WHITE = F9F5EF
    # RED = FD6574

window = Tk()
window.geometry("700x400")
window.title("Taxi Booking")
window.configure(bg='#6C8A9B')
myImg = ImageTk.PhotoImage(Image.open("taxi1.jpg"))
mylabel = Label(image=myImg)
mylabel.pack()

taxitxt = Label(window,text="CAB_MANDU",font= ("comicsansm",40,"bold"),bg="#6C8A9B",fg="#F9F5EF")
taxitxt.place(x=150,y=1)
#driver
txtDriver = Label(window,text=""" DRIVER """,font= ("comicsansm",15,"bold"),bg="lightslategrey",fg="#F9F5EF")
txtDriver.place(x=10,y=70)
def gotosignindriver():
    window.destroy()
    from driver.driverui import driverui

    driverui.__init__(self=window)
def gotosigninuser():
    window.destroy()
    from user.signinui import uisingnup
    uisingnup.__init__(self=window)

btnSignupd = Button(window, text="Signup",bg="#FD6574",command=gotosignindriver)
btnSignupd.place(x=20, y=100)

#user
txtUser = Label(window,text="""FIND A RIDE  """,font= ("comicsansm",15,"bold"),bg="lightslategrey",fg="#F9F5EF")
txtUser.place(x=300,y=70)
btnSignupc = Button(window, text="Signup",bg="#FD6574", command=gotosigninuser)
btnSignupc.place(x=325, y=100)
# login
btndLogin = Button(window, text="Login",bg="#FD6574",command=driverlogin)
btndLogin.place(x=100, y=100)
btnLogin = Button(window, text="Login",bg="#FD6574",command=login)
btnLogin.place(x=400, y=100)
#admin
txtAdmin = Label(window,text="""ADMIN  """,font= ("comicsansm",15,"bold"),bg="lightslategrey",fg="#F9F5EF")
txtAdmin.place(x=600,y=70)
btnloginad = Button(window, text="login",bg="#FD6574", command=adminui)
btnloginad.place(x=605, y=100)










window.mainloop()