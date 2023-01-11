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

taxitxt = Label(window,text="CAB_MANDU",font= ("comicsansm",35,"bold"),fg="black")
taxitxt.place(x=1,y=0,width=700)
#driver
txtDriver = Label(window,text=""" DRIVER """,font= ("comicsansm",15,"bold"),bg="black",fg="#F9F5EF")
txtDriver.place(x=10,y=180)
def gotosignindriver():
    window.destroy()
    from driver.driverui import driverui

    driverui.__init__(self=window)
def gotosigninuser():
    window.destroy()
    from user.signinui import uisingnup
    uisingnup.__init__(self=window)

btnSignupd = Button(window, text="Signup",bg="white",command=gotosignindriver)
btnSignupd.place(x=10, y=225)

#user
txtUser = Label(window,text=""" FIND A RIDE """,font= ("comicsansm",15,"bold"),bg="black",fg="#F9F5EF")
txtUser.place(x=300,y=180)
btnSignupc = Button(window, text="Signup",bg="white", command=gotosigninuser)
btnSignupc.place(x=300, y=225)
# login
btndLogin = Button(window, text="Login",bg="white",command=driverlogin)
btndLogin.place(x=80, y=225)
btnLogin = Button(window, text="Login",bg="white",command=login)
btnLogin.place(x=380, y=225)
#admin
txtAdmin = Label(window,text=""" ADMIN """,font= ("comicsansm",15,"bold"),bg="black",fg="#F9F5EF")
txtAdmin.place(x=600,y=180)
btnloginad = Button(window, text="Login",bg="white", command=adminui)
btnloginad.place(x=625, y=225)










window.mainloop()