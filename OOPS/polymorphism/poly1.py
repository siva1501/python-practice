class circle: #Original Method
    def draw(self):
        print("Draw the circle")
        
class Rectangle(circle):#overridder method
    def draw(self):
        print("Draw the rectangle")
        super().draw()
class square(Rectangle):#overridder method
    def draw(self):
        print("Draw the square")
        super().draw()
# s=circle()
# s.draw()
# s=Rectangle()
# s.draw()
s=square()
s.draw()
