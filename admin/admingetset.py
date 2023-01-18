"""set get for admin to store and retrive data from database"""
class adminsignup:
    def __init__(self,amail=None,apassword=None):

        self.amail = amail
        self.apassword = apassword


    def getAMAIL(self):
        return self.amail
    def getAPASSWORD(self):
        return self.apassword




    def setAMAIL(self,amail):
        self.amail=amail

    def setAPASSWORD(self,apassword):
         self.apassword=apassword


    def __str__(self):
        return ("{}, {}, {}, {}".format(self. self.amail , self.apassword, ))