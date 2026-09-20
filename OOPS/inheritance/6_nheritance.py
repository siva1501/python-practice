class GrandParent:
    def GrandParentProperty(self):
        self.gpp = float(input("Enter the Grand Parent Property:"))
        return self.gpp


class Parent:
    def ParentProperty(self):
        self.pp = float(input("Enter the Parent Property:"))
        return self.pp


class Child(GrandParent, Parent):
    def ChildProperty(self):
        gpp = self.GrandParentProperty()
        pp = self.ParentProperty()
        self.cp = gpp + pp
        print("*" * 50)
        print(
            "Total propert is grandparent{} and parent {} is chilold {}.".format(
                self.gpp, self.pp,self.gpp + self.pp 
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
s.ChildProperty()
