
from circle import Circle

class Controller:
    def __init__(self):
        size(600, 400)
        self.circlea = Circle(PVector(width/2, height/2), 100, PVector(2, 2))
        self.circleb = Circle(PVector(width/2, height/2), 100, PVector(3, 1))
        
    def draw(self):
        background(0, 0, 0)
        self.circlea.draw()
        self.circleb.draw()
        self.circlea.move()
        self.circleb.move()
