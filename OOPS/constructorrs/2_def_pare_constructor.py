# 1_def_pare_constructor.py
class Student:
    def __init__(self):
        self.sno = int(input("Enter The Student Number:"))
        self.sname = input("Enter the Student NameL:")


# main program
s = Student()
print("initial contant od s=", s.__dict__)
print("*" * 50)
s1 = Student()
print("initial contant od s1=", s1.__dict__)
print("*" * 50)
s2 = Student()
print("initial contant od s2=", s2.__dict__)
print("*" * 50)
