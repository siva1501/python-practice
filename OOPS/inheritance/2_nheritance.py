class c1:
    def setA(self):
        self.a = 10


class c2(c1):
    def setB(self):
        self.b = 20
        self.setA()  # calling bace class metyhod from derive class method
        self.disp()  # calling current class metyhod from oyher  method of current clsass

    def disp(self):
        print("val of a(c1-bc):{}".format(self.a))
        print("val of b(c2-dc):{}".format(self.b))
        print(
            "val of a(c2-dc):{} + b(c2-dc):{} is:{}".format(
                self.a, self.b, self.a + self.b
            )
        )


# main program

s = c2()
print("contant os s:", s.__dict__)
s.setB()
