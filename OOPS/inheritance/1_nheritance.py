# single inheritance
class c1:
    def setA(self):
        self.a = 10


class c2(
    c1
):  # single inheritance --= is called base class and c2 is called derived class
    def setB(self):
        self.b = 20

    def displ(self):
        print("val of a(c1-bc):{}".format(self.a))
        print("val of a(c1-dc):{}".format(self.b))
        print("sum of {} and {} is {}".format(self.a, self.b, self.a + self.b))


# main program
s = c2()
print("contant of s", s.__dict__)
s.setA()
print("contant of s", s.__dict__)
s.setB()
print("contant of s", s.__dict__)
s.displ()
