from tkinter import *
from driver.databasedriver import alldriver
from tkinter import ttk
class viewdriver():
    def __init__(self):

            window = Tk()
            window.geometry("700x400")
            window.configure(bg='#6C8A9B')
            drivers = alldriver()

            tableFrame = Frame(window)
            tableFrame.place(x=200, y=60)

            tblPersons = ttk.Treeview((tableFrame))
            tblPersons['columns'] = (('Name', 'Phone NO', 'Email'))

            tblPersons.column("#0", width=0, stretch=NO)
            tblPersons.column("Name", width=100, anchor=CENTER)
            tblPersons.column("Phone NO", width=100, anchor=CENTER)
            tblPersons.column("Email", width=150, anchor=CENTER)

            tblPersons.heading('#0', text='', anchor=CENTER)
            tblPersons.heading('Name', text='Name', anchor=CENTER)
            tblPersons.heading('Phone NO', text='Phone No', anchor=CENTER)
            tblPersons.heading('Email', text='Email', anchor=CENTER)

            for driver in drivers:
                tblPersons.insert(parent='', index='end', iid=driver[0],
                                  values=(driver[0], driver[1], driver[2]))
            tblPersons.pack()

            tblPersons.bind("<<TreeviewSelect>>")
            window.mainloop()
