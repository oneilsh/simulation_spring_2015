from agent import Agent

class MouseFollower(Agent):
    
    def findmouse(self):
        return PVector(mouseX, mouseY)
    

    def cognate(self, agents):
        mouse = self.findmouse()
        tomouse = self.pos - mouse
        if tomouse.mag() < self.sightdistance:
            self.seek(mouse)
            
    def draw(self):
        fill(200, 40, 40)
        stroke(255, 255, 255)
        #ellipse(self.pos.x, self.pos.y, 10, 10)
        pushMatrix()
        angle = atan2(self.speed.y, self.speed.x)
        translate(self.pos.x, self.pos.y)
        rotate(angle)
        
        rect(-15.0, -5.0, 30.0, 10.0)
        
        pushMatrix()  # whisker 1
        rotate(-1*PI/8)
        line(0.0, 0.0, 40.0, 0.0)
        popMatrix()
        
        pushMatrix()  # whisker 2
        rotate(PI/8)
        line(0.0, 0.0, 40.0, 0.0)
        popMatrix()
        
        popMatrix()
