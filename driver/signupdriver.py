
class Driversignup():
    def __int__(self,dname=None,dphone=None,dmail=None,dpassword=None,dliscenseno=None):
        self.dname=dname
        self.dphone = dphone
        self.dmail = dmail
        self.dpassword = dpassword
        self.dliscenseno = dliscenseno
    def getDNAME(self):
        return self.dname
    def getDPHONE(self):
        return self.dphone
    def getDMAIL(self):
        return self.dmail
    def getDPASSWORD(self):
        return self.dpassword
    def getDLISCENSENO(self):
        return self.dliscenseno

    def setDNAME(self,dname):
        self.dname =dname

    def setDPHONE(self,dphone):
         self.dphone=dphone

    def setDMAIL(self,dmail):
        self.dmail=dmail

    def setDPASSWORD(self,dpassword):
         self.dpassword=dpassword

    def setDLISCENSENO(self,dliscenseno):
        self.dliscenseno=dliscenseno
    def __str__(self):
        return ("{}, {}, {}, {}".format(self.dname, self.dphone, self.dmail , self.dpassword, self.dliscenseno))



