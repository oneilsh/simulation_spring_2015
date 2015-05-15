
from circle import Circle

class Controller:
    def __init__(self):
        size(600, 400)
        self.circles = list()
        for i in range(0,3):
            newcirc = Circle(PVector(random(0,width), random(0,height)), random(10,120), PVector(random(-3, 3), random(-3, 3)))
            self.circles.append(newcirc)
        
    def draw(self):
        background(0, 0, 0)
        for circle in self.circles:
            circle.draw()
            circle.apply_force(PVector(0, 0.5) / circle.mass)   # gravity, scales with mass
            if mousePressed:
                circle.apply_force(PVector(0.2, 0)) # wind :)
                
                ## below: gravitational attraction toward the mouse
                ## decreases with square of distance
                mousedir = PVector(mouseX, mouseY) - circle.pos
                distance = mousedir.mag()
                mousedir.normalize()
                mousedir = 500 * mousedir/(distance ** 2)
                circle.apply_force(mousedir / circle.mass)
                
            circle.move(self.circles)
            circle.reset_acceleration()

