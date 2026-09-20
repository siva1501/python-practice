class circle:#Original Method
    def draw(self):
        print("Draw the circle")
class Rectangle:#overridder method
    def draw(self):
        print("Draw the rectangle")
class square:#overridder method
    def draw(self):
        print("Draw the square")
s=circle()
s.draw()
s=Rectangle()
s.draw()
s=square()
s.draw()

