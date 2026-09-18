class test:
    def __init__(self, a, b):  # paremeterized_constuctor
        print("i am from paremeterized constuctor")
        self.a = a
        self.b = b
        print("value od a is {}".format(self.a))
        print("value od b is {}".format(self.b))


# main program
t1 = test(10, 20)
print("*" * 50)
t2 = test(10, 20)
print("*" * 50)
t3 = test(10, 20)
print("*" * 50)
