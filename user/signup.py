class Signup:
    def __init__(self,cname=None,cphone=None,cmail=None,cpassword=None):
        self.cname=cname
        self.cphone = cphone
        self.cmail = cmail
        self.cpassword = cpassword
    def getCNAME(self):
        return self.cname
    def getCPHONE(self):
        return self.cphone
    def getCMAIL(self):
        return self.cmail
    def getCPASSWORD(self):
        return self.cpassword

    def setCNAME(self,cname):
        self.cname =cname

    def setCPHONE(self,cphone):
         self.cphone=cphone

    def setCMAIL(self,cmail):
        self.cmail=cmail

    def setCPASSWORD(self,cpassword):
         self.cpassword=cpassword
    def __str__(self):
        return ("{}, {}, {}, {}".format(self.cname, self.cphone, self.cmail , self.cpassword))



