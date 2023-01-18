from tkinter import *
from driver.databasedriver import alldriver
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import mysql
class assigndriver():
    def __init__(self):
            # Gui to assign the driver
            window = Tk()
            window.geometry("700x400")
            window.configure(bg='grey')
            drivers = alldriver()
            # frame of table to display driver
            tableFrame = Frame(window)
            tableFrame.place(x=50, y=60)

            tblPersons = ttk.Treeview((tableFrame))
            tblPersons['columns'] = (('Did', 'Name', 'Phone NO', 'Email', 'licenseno'))

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
                                      values=(driver[0], driver[1], driver[2], driver[3], driver[4]))
            tblPersons.pack()







            def driv():
                    conn = mysql.connector.connect(host='localhost', user='root', password='', port="3306",
                                                   database='taxi')
                    cursor = conn.cursor()
                    query = """SELECT * FROM  drivers"""
                    cursor.execute(query)
                    result = cursor.fetchone()
                    if result:
                        messagebox.showinfo("Title","Driver Assigned Successfull")
                    else:
                        print("Driver not found")






            def selectId(self, _):
                    self.driverid = self.tblPersons.selection()[0]



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
            # button to assig the driver
            btnselectdriver = Button(window, text="Select Driver", font=("forte", 15,), command=driv)
            btnselectdriver.place(x=250, y=345)



            window.mainloop()
