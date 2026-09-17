# instance data members and class level data members

class Student:
    crs="PYTHON"
#main program
s1=Student()
s2=Student()
print("content of s1 bfore adding=",s1.__dict__)
print("content of s2 bfore adding=",s2.__dict__)

#Read instance data member such as  sno and sname and smarks to s1
print("First Student information")
print("-"*50)
s1.sno=int(input("Enter the Student number:"))
s1.sname=input("Enter the Student name:")
s1.marks=float(input("Enter the Student Marks:"))

print("-"*50)
print("First Student information")
print("-"*50)
s2.sno=int(input("Enter the Student number:"))
s2.sname=input("Enter the Student name:")
s2.marks=float(input("Enter the Student Marks:"))
print("-"*50)
print("content of s1 after adding=",s1.__dict__)
print("content of s2 after adding=",s2.__dict__)
