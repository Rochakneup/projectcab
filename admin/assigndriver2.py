from tkinter import *
from driver.databasedriver import alldriver
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
class assigndriver():
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
            tblPersons.bind("<<TreeviewSelect>>")
            for driver in drivers:
                tblPersons.insert(parent='', index='end', iid=driver[0],
                                  values=(driver[0], driver[1], driver[2]))
            tblPersons.pack()


            btnselectdriver = Button(window, text="Select Driver", font=("forte", 15,))
            btnselectdriver.place(x=250, y=345)

            def selectId(self, _):
                    self.driverid = self.tblPersons.selection()[0]

                    btnAssign = Button(self.root, text="Select Driver", background="#ff9999", command=self.selectDriver)
                    btnAssign.place(x=800, y=600)

            def selectDriver(self):
                    print(self.driverid, self.tripid)
                    if not self.driverid:
                            return
                    sql = "UPDATE allbooking SET did=%s, status= 'confirm' WHERE tid=%s"
                    values = (self.driverid, self.tripid)
                    self.root.destroy()
                    messagebox.showinfo("Success", "Driver assigned successfully")
                    record = None

                    conn = mysql.connector.connect(
                            host='localhost',
                            port='3306',
                            user='root',
                            password='',
                            database='yourstaxi'
                    )
                    cursor = conn.cursor()
                    cursor.execute(sql, values)
                    conn.commit()
                    cursor.close()
                    conn.close()

            window.mainloop()