#main program
class Student:pass
s1=Student()
s2=Student()
print("content of s1 before adding the data={} and number of values={}".format(s1.__dict__,len(s1.__dict__)))
print("content of s2 before adding the data={} and number of values={}".format(s2.__dict__,len(s2.__dict__)))

#Adding instance data member s1

s1.sno=10
s1.name="siva"
s1.marks=55.55
print("content of s1 after adding the data={} and number of values={}".format(s1.__dict__,len(s1.__dict__)))

#Adding instance data member s2

s2.sno=10
s2.sname="siva"
s2.smarks=55.55
print("content of s2 aftre adding the data={} and number of values={}".format(s2.__dict__,len(s2.__dict__)))
