class grandparent:
    def grandparantpro(self):
        self.gpp = 15.5


class parant(grandparent):
    def parentpro(self):
        self.pp = 45.5


class child(parant):
    def childpro(self):
        self.cp = 100.5

    def totalpro(self):
        self.grandparantpro()
        self.parentpro()
        self.childpro()
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
s = child()
s.totalpro()
