# instance method
class Student:
    crs = "PYTHON"

    def getstudentdata(self):
        print("-" * 50)
        self.sno = int(input("Enter the Number of Student:"))
        self.sname = input("Enter The Name of Student:")
        self.smarks = float(input("Enter the Marks of Student:"))
        print("-" * 50)
        self.dispalystudentdata()  # calling instance method from anther instance method

    def dispalystudentdata(self):
        print("-" * 50)
        print(" Number of Student:{}".format(self.sno))
        print(" Name of Student:{}".format(self.sname))
        print(" marks of Student:{}".format(self.smarks))
        print(" Courese of Student:{}".format(self.crs))
        print("-" * 50)


# main program
s1 = Student()
s2 = Student()
print("Contenrt os s1 before adding=", s1.__dict__)
print("Contenrt os s2 before adding=", s2.__dict__)
print("-" * 50)
print("Enter the first Student  Information")
s1.getstudentdata()
print("Enter the second Student  Information")
s2.getstudentdata()
print("-" * 50)
