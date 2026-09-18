class test:
    def __init__(self):
        print("i am from default constuctor")
        self.a = 10
        self.b = 20
        print("value od a is {}".format(self.a))
        print("value od b is {}".format(self.b))


# main program
t1 = test()
print("*" * 50)
t2 = test()
print("*" * 50)
t3 = test()
print("*" * 50)
