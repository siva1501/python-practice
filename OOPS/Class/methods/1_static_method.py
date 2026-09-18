class Student:
    def getstuedentdata(self):
        self.sno = int(input("Enter the student number:"))
        self.sname = input("Enter the student name:")
        self.course = input("Eneter the studnt course:")


class Employe:
    def getemployedeta(self):
        self.eno = int(input("Enter the employe number:"))
        self.ename = input("Enter the employe name:")
        self.eal = float(input("Eneter the employe salare:"))


class techer:
    def gettecherdata(self):
        self.tno = int(input("Enter the teacher number:"))
        self.tyame = input("Enter the teacher name:")
        self.eal = float(input("Eneter the teacher salare:"))


class hyd:
    @staticmethod
    def dispoobjectdata(ksr, pinfo):
        print("*" * 100)
        print("information about {}".format(pinfo))
        for k, s in ksr.__dict__.items():
            print("\t {}  {}".format(k, s))
        print("*" * 100)


# main program
s = Student()
e = Employe()
t = techer()
s.getstuedentdata()
e.getemployedeta()
t.gettecherdata()
# call static method w r t class name
hyd.dispoobjectdata(s, "Student")
hyd.dispoobjectdata(e, "Employe")
hyd.dispoobjectdata(t, "techer")
