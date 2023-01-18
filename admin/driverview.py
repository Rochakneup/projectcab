from tkinter import *
from driver.databasedriver import alldriver
from tkinter import ttk
class viewdriver():
    def __init__(self):
            # GUi to view all drivers
            window = Tk()
            window.geometry("700x400")
            window.configure(bg='grey')
            drivers = alldriver()
            txtLogin = Label(window, text="DRIVERS ", font=("comicsansm", 30, "bold"), bg="grey", fg="black")
            txtLogin.place(x=200, y=10)
            # frame to display table of all the drivers
            tableFrame = Frame(window)
            tableFrame.place(x=50, y=60)

            tblPersons = ttk.Treeview((tableFrame))
            tblPersons['columns'] = (('Did','Name', 'Phone NO', 'Email','licenseno'))

            tblPersons.column("#0", width=0, stretch=NO)
            tblPersons.column("Did", width=100, anchor=CENTER)
            tblPersons.column("Name", width=100, anchor=CENTER)
            tblPersons.column("Phone NO", width=100, anchor=CENTER)
            tblPersons.column("Email", width=150, anchor=CENTER)
            tblPersons.column("licenseno", width=150, anchor=CENTER)
            tblPersons.heading('#0', text='', anchor=CENTER)
            tblPersons.heading('Did', text='Did', anchor=CENTER)
            tblPersons.heading('Name', text='Name', anchor=CENTER)
            tblPersons.heading('Phone NO', text='Phone No', anchor=CENTER)
            tblPersons.heading('Email', text='Email', anchor=CENTER)
            tblPersons.heading('licenseno', text='Licenseno', anchor=CENTER)
            for driver in drivers:
                tblPersons.insert(parent='', index='end', iid=driver[0],
                                  values=(driver[0], driver[1], driver[2],driver[3],driver[4]))
            tblPersons.pack()

            tblPersons.bind("<<TreeviewSelect>>")
            window.mainloop()
