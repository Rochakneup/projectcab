from tkinter import *
from tkinter import ttk
from user.datauser import alluser
class viewcustomer():
    # GUi to view all customer
    def __init__(self):
        window = Tk()
        window.geometry("700x400")
        window.configure(bg='grey')
        users = alluser()
        txtLogin = Label(window, text="CUSTOMERS  ", font=("comicsansm", 30, "bold"), bg="grey", fg="black")
        txtLogin.place(x=200, y=10)
        # frame of table to display all the users
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


        for user in users :
            tblPersons.insert(parent='', index='end', iid=user[0],
                              values=(user[1], user[2], user[3]))
        tblPersons.pack()

        tblPersons.bind("<<TreeviewSelect>>")
