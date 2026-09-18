class Student:
    def __init__(self, sno, sname):  # paremeterized_constuctor
        self.sno = sno
        self.sname = sname


# main program
s1 = Student(1, "siva")
print("inital Contant of s1=", s1.__dict__)
print("*" * 50)
s2 = Student(2, "Harshi")
print("inital Contant of s2", s2.__dict__)
print("*" * 50)
s3 = Student(3, "Nani")
print("inital Contant of s3=", s3.__dict__)
print("*" * 50)
