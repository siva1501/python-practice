class GrandParent:
    def GrandParentProperty(self):
        self.gpp = float(input("Enter the Grand Parent Property:"))


class Parent(GrandParent):
    def ParentProperty(self):
        self.pp = float(input("Enter the Parent Property:"))


class Child(Parent):
    def ChildProperty(self):
        self.cp = float(input("Enter the child Property:"))

    def TotalProperty(self):
        self.GrandParentProperty()
        self.ParentProperty()
        self.ChildProperty()
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
s = Child()
s.TotalProperty()
