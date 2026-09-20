class circle:
    def  __init__(self):
        print("drawing circl")
class rect(circle):
    def __init__(self):
        print("Drowing rectangle")
        super().__init__()
class square(rect):
    def __init__(self):
        print("Drowing square")
        super().__init__()
# main program
s=square()
