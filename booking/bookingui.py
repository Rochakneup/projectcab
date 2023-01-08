from tkinter import *
from PIL import ImageTk, Image
from booking.bookingdatabae import bookings
#
class booking():
    def __init__(self):
        window = Tk()
        window.geometry("700x400")
        window.title("Taxi Booking")
        window.configure(bg='#6C8A9B')


        txtBooking = Label(window,text="MAKE BOOKING",font= ("comicsansm",20,"bold"),bg="#6C8A9B",fg="#F9F5EF")
        txtBooking.place(x=250,y=1)
        lblpickadd = Label(window, text="Pick-up Address: ",bg="#6C8A9B", font=("Times New Roman", 13))
        lblpickadd.place(x=200, y=70)
        lblpickadd.configure(bg="#6C8A9B")
        txtpickadd = Entry(window, width=20)
        txtpickadd.place(x=350, y=70, height=20)

        lbldropadd = Label(window, text="Pick-up Time: ", font=("Times New Roman", 13))
        lbldropadd.place(x=200, y=120)
        lbldropadd.configure(bg="#6C8A9B")
        txtdropadd = Entry(window, width=20)
        txtdropadd.place(x=350, y=120, height=20)

        lblpicktime = Label(window, text="Drop-off Address: ", font=("Times New Roman", 13))
        lblpicktime.place(x=200, y=170)
        lblpicktime.configure(bg="#6C8A9B")
        txtpicktime = Entry(window, width=20)
        txtpicktime.place(x=350, y=170, height=20)

        lblpickdate = Label(window, text="Pick-up Date: ", font=("Times New Roman", 13))
        lblpickdate.place(x=200, y=220)
        lblpickdate.configure(bg="#6C8A9B")
        txtpickdate = Entry(window, width=20)
        txtpickdate.place(x=350, y=220, height=20)



        def savebooking():
            # reading value from entry and send to library/middleware
            pickupaddress = (txtpickadd.get())
            pickuptime = (txtpicktime.get())
            dropaddress = (txtdropadd.get())
            pickupdate = (txtpickdate.get())

            result = bookings(pickupaddress,pickuptime,dropaddress,pickupdate)
            if (result == True):
                print("Error to insert")
            else:
                print("booking done!")


        btnConfirm = Button(window, text="Confirm Booking", command=savebooking, font=("Times New Roman", 14),
                                bg="#FD6574", )
        btnConfirm.place(x=250, y=300)
        btnCancel = Button(window, text="Cancel Booking", command=savebooking, font=("Times New Roman", 14),
                            bg="#FD6574", )
        btnCancel.place(x=400, y=300)

        btnedit = Button(window, text="Edit Booking", command=savebooking, font=("Times New Roman", 14),
                           bg="#FD6574", )
        btnedit.place(x=550, y=300)




        window.mainloop()

