class Student:
    def getstudentdata(self):
        print("-" * 50)
        self.sno = int(input("Enter the Student Number:"))
        self.sname = input("Enter the Student neme:")
        self.smarks = float(input("Enter the Student Number:"))
        print("-" * 50)

    def displstudentdata(hyd):
        print("-" * 50)
        print("\t Student Nmber:{}".format(hyd.sno))
        print("\t Student Name:{}".format(hyd.sname))
        print("\t Student marks:{}".format(hyd.smarks))
        print("-" * 50)


# main progream
s1 = Student()
s2 = Student()
print("contert of s1 before information=", s1.__dict__)
print("contert of s1 before information=", s2.__dict__)
print("-" * 50)
print("Enter the firdt student infiormation")
s1.getstudentdata()
print("Enter the Second student infiormation")
s2.getstudentdata()
print("Details of firdt student")
s1.displstudentdata()
print("Details of second student")
s2.displstudentdata()
