# profram for demonstrating Class level method and class level data members
class Student:
    @classmethod
    def getcorude(cls):
        cls.crs = "PYTHON"

    @classmethod
    def getDevalop(cls):
        Student.dev = "SIVA"


# main program
s1 = Student()
s2 = Student()
s1.getcorude()  # calling class level method writ class name
s2.getDevalop()  # calling class level method writ class name
print(s1.crs, s1.dev)
print(s2.crs, s2.dev)
