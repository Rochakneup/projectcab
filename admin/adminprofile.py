from tkinter import *
from admin.assigndriver import driverassign
from admin.customerview import viewcustomer
from admin.driverview import viewdriver
from admin.allbokingview import viewallbookings
class profile():
    def __init__(self):
        window = Tk()
        window.geometry("700x400")
        window.configure(bg='#6C8A9B')
        assigndriver = Button(window, text="Assign Driver", command=driverassign, bg="#FD6574",)
        assigndriver.place(x=100, y=100)
        customer = Button(window, text="View Customer", command=viewcustomer, bg="#FD6574", )
        customer.place(x=200, y=100)
        driver = Button(window, text="View Driver", command=viewdriver, bg="#FD6574", )
        driver.place(x=300, y=100)
        bookings = Button(window, text="View All Bookings", command=viewallbookings, bg="#FD6574", )
        bookings.place(x=400, y=100)


        window.mainloop()
