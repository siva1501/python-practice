import time
class Student:
    def __init__(self,sno,sname):
        print("I am frtom pc")
        self.sno=sno
        self.sname=sname
        print("\t{}\t{}".format(self.sno,self.sname))
    def __del__(self):
        print("GC call__del__")
   

#Mmain program
print("\n Program execution started")
s1=Student(10,"ravi")#object created
print("Now we are No Longer interested in maintaing S1 object memory space")
time.sleep(5)
s2=Student(20,"ram")#object created
print("\n Program execution ended")
time.sleep(5)