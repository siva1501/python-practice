# profram for demonstrating Class level method and class level data members
class Student:
    @classmethod
    def getCourse(cls):
        cls.cru = "PYTHON"
        cls.getDevlop("Siva")  # calling class level method write cls

    @classmethod
    def getDevlop(cls, dname):
        Student.dev = dname

    def getstudentdec(self, sno, sname, smarks):
        self.sno = sno
        self.sname = sname
        self.smarks = smarks

    def dispstudentdata(self):
        self.getCourse()  # calling class level method name write self

        print("Student number={}".format(self.sno))
        print("Student name={}".format(self.sname))
        print("Student marks={}".format(self.smarks))
        print("Student Courese={}".format(self.cru))
        print("Student developer={}".format(self.dev))


# main program
s1 = Student()
s2 = Student()
s1.getstudentdec(1, "siva", 55.5)
s2.getstudentdec(2, "nani", 65.5)
s1.dispstudentdata()
s2.dispstudentdata()
