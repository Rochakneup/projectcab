from tkinter import *
from admin.assigndriver import driverassign
from admin.customerview import viewcustomer
from admin.driverview import viewdriver
from admin.allbokingview import viewallbookings

class profile():
    def __init__(self):
        # gui for admin profile
        window = Tk()
        window.geometry("700x400")
        window.configure(bg='grey')
        # button to assign driver
        assigndriver = Button(window, text="Assign Driver", font= ("comicsansm",20,"bold"),command=driverassign, bg="black",fg='white')
        assigndriver.place(x=200, y=50)
        # button to view all customer
        customer = Button(window, text="View Customer",font= ("comicsansm",20,"bold"),command=viewcustomer, bg="black",fg='white' )
        customer.place(x=200, y=125)
        # button to view all drivers
        driver = Button(window, text="View Driver",font= ("comicsansm",20,"bold"), command=viewdriver, bg="black",fg='white' )
        driver.place(x=200, y=200)
        # button to view all bookings
        bookings = Button(window, text="View All Bookings",font= ("comicsansm",20,"bold"), command=viewallbookings, bg="black",fg='white' )
        bookings.place(x=200, y=275)


        logout = Button(window, text="LOgout", font=("comicsansm", 10, "bold"), bg="black", fg='white')
        logout.place(x=100, y=275)

        window.mainloop()
