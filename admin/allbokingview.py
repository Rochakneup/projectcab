from tkinter import *
from tkinter import ttk
from booking.bookingdatabae import all

# gui for admin to view all booking
class viewallbookings():
    def __init__(self):
        window = Tk()
        window.geometry("700x400")
        window.configure(bg='grey')
        # label for all bookings
        trips = all()
        txtLogin = Label(window, text="ALL BOOKINGS  ", font=("comicsansm", 30, "bold"), bg="grey", fg="black")
        txtLogin.place(x=200, y=10)
        # frame for the table to display all boking
        tableFrame = Frame(window)
        tableFrame.place(x=50, y=60)

        tblPersons = ttk.Treeview((tableFrame))
        tblPersons['columns'] = (('Tid', 'Pickup', 'Dropoff', 'Time', 'Date','Status'))

        tblPersons.column("#0", width=0, stretch=NO)
        tblPersons.column("Tid", width=100, anchor=CENTER)
        tblPersons.column("Pickup", width=100, anchor=CENTER)
        tblPersons.column("Dropoff", width=100, anchor=CENTER)
        tblPersons.column("Time", width=100, anchor=CENTER)
        tblPersons.column("Date", width=100, anchor=CENTER)
        tblPersons.column("Status", width=100, anchor=CENTER)

        tblPersons.heading('#0', text='', anchor=CENTER)
        tblPersons.heading('Tid', text='TID', anchor=CENTER)
        tblPersons.heading('Pickup', text='PICKUP', anchor=CENTER)
        tblPersons.heading('Dropoff', text='DROPOFF', anchor=CENTER)
        tblPersons.heading('Time', text='TIME', anchor=CENTER)
        tblPersons.heading('Date', text='DATE', anchor=CENTER)
        tblPersons.heading('Status', text='Status', anchor=CENTER)
        for trip in trips:
            tblPersons.insert(parent='', index='end', iid=trip[0], values=(trip[0], trip[1], trip[2], trip[3], trip[4],trip[5]))
        tblPersons.pack()

        tblPersons.bind("<<TreeviewSelect>>")
