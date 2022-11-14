class Student:

    def getdata(self,fname,lname):
        print("getdata Called")
        self.f=fname
        self.l=lname
    def putdata(self):
        print("First Name : ",self.f)
        print("Last Name : ",self.l)

s1=Student()
fname=input("Enter First Name: ")
lname=input("Enter Last Name : ")
s1.getdata(fname,lname)
s1.putdata()
