
"""set get for booking to store and retrive data """
class allbooking:
    def __int__(self,pickupaddress=None,pickuptime=None,dropaddress=None,pickupdate=None):
        self.pickupaddress=pickupaddress
        self.pickuptime = pickuptime
        self.dropaddress = dropaddress
        self.pickupdate= pickupdate
    def getpickupaddress(self):
        return self.pickupaddress
    def getpickuptime(self):
        return self.pickuptime
    def getdropaddress(self):
        return self.dropaddress
    def getpickupdate(self):
        return self.pickupdate

    def setpickupaddress(self):
        return self.pickupaddress
    def setpickuptime(self):
        return self.pickuptime
    def setdropaddress(self):
        return self.dropaddress
    def setpickupdate(self):
        return self.pickupdate

    def __str__(self):
        return ("{}, {}, {}, {}".format(self.pickupaddress,self.pickuptime,self.dropaddress,self.pickupdate))