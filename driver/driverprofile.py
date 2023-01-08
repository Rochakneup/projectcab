from tkinter import *
from driver.viewbooking import viewbooking
from driver.alltrip import trip

class driverprofile():
    def __init__(self):
        window = Tk()
        window.title("Login")
        window.geometry("700x400")
        window.configure(bg='#6C8A9B')
        txtProfile = Label(window, text="PROFILE  ", font=("comicsansm", 35, "bold"), bg="#6C8A9B", fg="#F9F5EF")
        txtProfile.place(x=250, y=1)
        viewbookingbtn=Button(window,text="VIEW BOOKING",command=viewbooking,bg="#FD6574", )
        viewbookingbtn.place(x=300,y=200)
        tripbtn=Button(window,text="TRIP HISTORY",command=trip,bg="#FD6574")
        tripbtn.place(x=100,y=200)
        editbtn=Button(window,text="EDIT PROFILE",command=trip,bg="#FD6574")
        editbtn.place(x=500,y=200)
        window.mainloop()