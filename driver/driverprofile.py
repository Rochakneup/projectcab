from tkinter import *
from tkinter import ttk
from booking.bookingdatabae import all
import mysql.connector
from tkinter import messagebox
# GUI class for a driver to view their bookings
class driverprofile():
    def __init__(self):
        window = Tk()
        window.geometry("700x400")
        window.resizable(False, False)
        window.title("Insert New Trip")
        window.configure(bg='grey')
        trips = all()
        frame = Frame(window)
        frame.configure(bg="grey")
        frame.place(x=50, y=45)
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

        def change_status_to_completed():
            connection = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database='taxi'

            )
            cursor = connection.cursor()
            cursor.execute("UPDATE allbooking SET status='Completed'" )
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Trip Completed", )
            tblPersons.delete(*tblPersons.get_children())
            driv = all()
            for driv in driv:
                tblPersons.insert(parent='', index='end', iid=driv[0],
                             values=(driv[0], driv[1], driv[2], driv[3], driv[4],driv[5]))
            tblPersons.pack()
        btntrip = Button(window, text="Completed", font=("forte", 15,), command=change_status_to_completed)
        btntrip.place(x=250, y=345)
        btnlogout = Button(window, text="Logout", font=("forte", 10,), command=change_status_to_completed)
        btnlogout.place(x=150, y=345)
        window.mainloop()