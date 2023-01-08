from tkinter import *
from tkinter import ttk
from booking.bookingdatabae import allTrip

class previousbooking():
    def __init__(self):
        window = Tk()
        window.title("Login")
        window.geometry("700x400")
        window.configure(bg='#6C8A9B')


        frame1 = Frame(window)
        frame1.pack()
        trips = allTrip()
        tblPersons = ttk.Treeview(frame1)
        tblPersons['columns'] = ('PickupAddress', 'PickupTime', 'DropoffAddress','PickupDate')

        tblPersons.column("#0", width=0, stretch=NO)
        tblPersons.column("PickupAddress", width=100, anchor=CENTER)
        tblPersons.column("PickupTime", width=100, anchor=CENTER)
        tblPersons.column("DropoffAddress", width=150, anchor=CENTER)
        tblPersons.column("PickupDate", width=100, anchor=CENTER)

        tblPersons.heading("#0", text="", anchor=CENTER)
        tblPersons.heading("PickupAddress", text="Pickup Address", anchor=CENTER)
        tblPersons.heading("PickupTime", text="Pickup Time", anchor=CENTER)
        tblPersons.heading("DropoffAddress", text="Dropoff Address", anchor=CENTER)
        tblPersons.heading("PickupDate", text="Pickup Date", anchor=CENTER)
        # if tblPersons is not None:
        for trip in trips:
            tblPersons.insert(parent='', index='end', iid=trip[0],values=(trip[0], trip[1], trip[2], trip[3]))
            tblPersons.pack()


