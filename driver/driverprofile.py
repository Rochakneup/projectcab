from tkinter import *


class driverprofile():
    def __init__(self):
        window = Tk()
        window.title("Login")
        window.geometry("700x400")
        window.configure(bg='#6C8A9B')
        txtProfile = Label(window, text="PROFILE  ", font=("comicsansm", 35, "bold"), bg="#6C8A9B", fg="#F9F5EF")
        txtProfile.place(x=250, y=1)

        window.mainloop()