from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from booking.bookingdatabae import allTrip,all
from admin.driverview import viewdriver
from admin.assigndriver2 import assigndriver
class driverassign():
    def __init__(self):


            window = Tk()
            window.geometry("700x400")
            window.resizable(False, False)
            window.title("Insert New Trip")
            window.configure(bg='grey')
            trips = all()
            frame = Frame(window)
            frame.configure(bg="grey")
            frame.place(x=80, y=45)
            frame.configure(width=550, height=300)
            tblPersons = ttk.Treeview((frame))
            tblPersons['columns'] = (('Tid', 'Pickup', 'Dropoff', 'Time', 'Date', 'Status'))

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
                tblPersons.insert(parent='', index='end', iid=trip[0],
                                  values=(trip[0], trip[1], trip[2], trip[3], trip[4], trip[5]))
            tblPersons.pack()


            lbltitle = Label(window, text='Assign Driver', font=("forte", 20,), fg='black', bg="white")
            lbltitle.place(x=250, y=5)

            btnAssignDriver = Button(window, text="Assign Driver",font=("forte", 15,),command=assigndriver)
            btnAssignDriver.place(x=250, y=345)



            window.mainloop()



