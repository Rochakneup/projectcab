from tkinter import *
from tkinter import ttk

class triphistory():
    def __init__(self):
        window = Tk()
        window.geometry("700x400")
        window.title("Taxi Booking")
        window.configure(bg='#6C8A9B')
        # trips = allTrips()

        def displayAll():

            tableFrame = Frame(window)
            tableFrame.place(x=250, y=200)

            tblPersons = ttk.Treeview((tableFrame))
            tblPersons['columns'] = (('Pickup', 'Dropoff', 'Time', 'Date', 'Payment'))

            tblPersons.column("#0", width=0, stretch=NO)
            tblPersons.column("Pickup", width=100, anchor=CENTER)
            tblPersons.column("Dropoff", width=100, anchor=CENTER)
            tblPersons.column("Time", width=100, anchor=CENTER)
            tblPersons.column("Date", width=100, anchor=CENTER)
            tblPersons.column("Payment", width=100, anchor=CENTER)

            tblPersons.heading('#0', text='', anchor=CENTER)
            tblPersons.heading('Pickup', text='PICKUP', anchor=CENTER)
            tblPersons.heading('Dropoff', text='DROPOFF', anchor=CENTER)
            tblPersons.heading('Time', text='TIME', anchor=CENTER)
            tblPersons.heading('Date', text='DATE', anchor=CENTER)
            tblPersons.heading('Payment', text='PAYMENT', anchor=CENTER)
            # for trip in trips:
            #     tblPersons.insert(parent='', index='end', iid=trip[0], values=(trip[0], trip[1], trip[2], trip[3], trip[4]))
            # tblPersons.pack()


        displayAll()

        window.mainloop()
