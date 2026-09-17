#Class level method
class Studen:
    @classmethod
    def getcourse(cls):
       cls.crs="PYTHON "
    @classmethod
    def getDeveloper(cls):
      Studen.dev="Siva"

#main program 
Studen.getcourse()#calling class level method writ class name
Studen.getDeveloper()#calling class level method writ class name
s1=Studen()
s2=Studen()
print(s1.crs,s1.dev)
print(s2.crs,s2.dev)