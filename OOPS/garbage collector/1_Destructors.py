import sys
class Student:
    def __init__(self,sno,sname):
        print("I am frtom pc")
        self.sno=sno
        self.sname=sname
        print("\t{}\t{}".format(self.sno,self.sname))
    def __del__(self):
        global totmem
        print("GC call__del__")
        print("At Prtesent memory Space:{}".format(totmem))
        print("Now Memory space:",sys.getsizeof(self))
        totmem=totmem-sys.getsizeof(self)
        print("Remaing Memory Space:{}".format(totmem))

#Mmain program
print("\n Program execution started")
s1=Student(10,"ravi")#object created
s2=Student(20,"ram")#object created
totmem=sys.getsizeof(s1)+sys.getsizeof(s2)
print("Now Memory space:{}".format(totmem))
print("\n Program execution ended")
