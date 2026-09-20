class Grandprant:
    def grandprantprop(self):
        self.gpp = 15.5


class prant(Grandprant):
    def prantprop(self):
        self.pp = 45.5


class chilld(prant):
    def chilldprop(self):
        self.cp = 100.15

    def totalprop(self):
        print("*" * 50)
        print(
            "Total propert is grandparent{} and parent {} and chilold {} is:{}.".format(
                self.gpp, self.pp, self.cp, self.gpp + self.pp + self.cp
            )
        )
        print("*" * 50)
        print("Grand parant propert:{}".format(self.gpp))
        print("*" * 50)
        print("Parant propert:{}".format(self.pp))
        print("*" * 50)
        print("chailld propert:{}".format(self.cp))
        print("*" * 50)


# main program
s = chilld()
s.chilldprop()
s.grandprantprop()
s.prantprop()
s.totalprop()
