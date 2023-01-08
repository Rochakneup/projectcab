

from tkinter import messagebox
from tkinter import *

from tkinter import ttk
from tkinter import Tk, Label, Entry, Button

from booking.bookingdatabae import  allTrip,bookings,updateTrip

class windowTrip():
    def __init__(self):


            def save():
                # reading value from entry and send to library/middleware
                pickup = txtPickup.get()
                dropoff = txtDropoff.get()
                time = txtTime.get()
                date = txtDate.get()
                #
                result = bookings(pickupaddress=pickup,dropaddress=dropoff,pickuptime=time,pickupdate=date)
                if (result == None):
                    messagebox.showinfo("Title", "Trip Booked Sucessfully")
                    print("Insert Sucessfully")
                    trips = allTrip()
                    tblPersons.delete(*tblPersons.get_children())
                    for trip in trips:
                        tblPersons.insert(parent='', index='end', iid=trip[0],
                                          values=(trip[0], trip[1], trip[2], trip[3],trip[4],trip[5]))
                    tblPersons.pack()


                else:
                    messagebox.showerror("Title", "Trip not Booked")
                    print("Error to insert")

            # def update():
            #     # reading value from entry and send to library/middleware
            #     pickup = txtPickup.get()
            #     dropoff = txtDropoff.get()
            #     time = txtTime.get()
            #     date = txtDate.get()
            #     tid = tblPersons.selection()[0]
            #     result = updateTrip(pickup,dropoff,time, date,tid)
            #     if (result != None):
            #         messagebox.showinfo("Title", "Trip Updatede")
            #         print("Insert Sucessfully")
            #         trips = allTrip()
            #         tblPersons.delete(*tblPersons.get_children())
            #         for trip in trips:
            #             tblPersons.insert(parent='', index='end', iid=trip[0],
            #                               values=(trip[0], trip[1], trip[2], trip[3], trip[4], trip[5]))
            #         tblPersons.pack()
            #     else:
            #         messagebox.showerror("Title", "Trip not updated")
            #         print("Error to insert")

            def Update():
                pickup = txtPickup.get()
                time = txtTime.get()
                drop = txtDropoff.get()

                date = txtDate.get()
                tid = tblPersons.selection()[0]
                result = updateTrip(pickup, time, drop, date, tid)
                if result == True:
                    print("Record Edit")
                    messagebox.showinfo("Title", "Successfully Edited")
                    tblPersons.delete(*tblPersons.get_children())
                    trips = allTrip()
                    for trip in trips:
                        tblPersons.insert(parent='', index='end', iid=trip[0],
                                            values=((trip[0], trip[1], trip[2], trip[3], trip[4], trip[5])))
                        tblPersons.pack()
                else:
                    messagebox.showinfo("Title", "Edit Failed")
                    print("Error to Edit")

            # Declare and Initialize
            window = Tk()
            window.geometry("700x400")
            window.title("Insert New Trip")
            window.configure(bg='#6C8A9B')


            lblPickup = Label(window, text="Pickup", bg="#CAC2B5")
            lblDropoff = Label(window, text="DROPOFF", bg="#CAC2B5")
            lblTime = Label(window, text="TIME", bg="#CAC2B5")
            lblDate = Label(window, text="DATE", bg="#CAC2B5")

            txtTid = Entry(window, width=20)
            txtPickup = Entry(window, width=20)
            txtDropoff = Entry(window, width=20)
            txtTime = Entry(window, width=20)
            txtDate = Entry(window, width=20)

            btnSave = Button(window, text="Save",font=("Arial",10), bg="#FD6574", fg="#F8F8FF",command=save)
            btnClose = Button(window, text="Cancel",font=("Arial",10), bg="#FD6574", fg="#F8F8FF",command = window.destroy)
            btnedit = Button(window, text="Edit Booking",font=("Arial",10), bg="#FD6574", fg="#F8F8FF",command=Update)

            # cal = DateEntry(window, width=12, year=2023, month=1, day=1, background='#4D243D', foreground='white',borderwidth=2)
            # cal.place(x=100, y=100)



            lblPickup.place(x=300, y=10)
            txtPickup.place(x=380, y=10)

            lblDropoff.place(x=300, y=40)
            txtDropoff.place(x=380, y=40)

            lblTime.place(x=300, y=70)
            txtTime.place(x=380, y=70)

            lblDate.place(x=300, y=100)
            txtDate.place(x=380, y=100)

            btnClose.place(x=350, y=130)
            btnSave.place(x=420, y=130)
            btnedit.place(x=470, y=130)


            def clear():
                txtPickup.delete(0, END)
                txtDropoff.delete(0, END)
                txtTime.delete(0, END)
                txtDate.delete(0, END)

            btnclear = Button(window, text="clear", font=("Arial", 10), bg="#FD6574", fg="#F8F8FF", command=clear)
            btnclear.place(x=300, y=130)

            trips = allTrip()


            tableFrame = Frame(window)
            tableFrame.place(x=100, y= 160)

            tblPersons = ttk.Treeview((tableFrame))
            tblPersons['columns'] = (('Tid','Pickup', 'Dropoff', 'Time', 'Date','Status'))

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

            def displaySelectedItem(event):
                selectedItems = tblPersons.selection()
                if selectedItems:
                    selectedItem = selectedItems[0]
                    txtPickup.insert(0, tblPersons.item(selectedItem)['values'][1])
                    txtDropoff.insert(0, tblPersons.item(selectedItem)['values'][2])
                    txtTime.insert(0, tblPersons.item(selectedItem)['values'][3])
                    if len(tblPersons.item(selectedItem)['values']) > 4:
                        txtDate.insert(0, tblPersons.item(selectedItem)['values'][4])

            tblPersons.bind("<<TreeviewSelect>>", displaySelectedItem)

            window.mainloop()
windowTrip()