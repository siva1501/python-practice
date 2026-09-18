class test:
    def __init__(self, a=10, b=20):
        print("i am from paremeterized constuctor")
        self.a = a
        self.b = b
        print("value od a is {}".format(self.a))
        print("value od b is {}".format(self.b))


# main program
t1 = test()
print("*" * 50)
t2 = test(100, 200)
print("*" * 50)
t3 = test(1000, 2000)
print("*" * 50)
