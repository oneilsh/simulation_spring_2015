
class Particle:
    def __init__(self, initialpos):
        self.pos = initialpos
        self.speed = PVector(0.0, 0.0)
        
    def draw(self):
        fill(0,0,0)
        stroke(255, 255, 255)
        ellipse(self.pos.x, self.pos.y, 5, 5)
        
        

        
    def move(self):
        self.speed.x = randomGaussian() * 2
        self.speed.y = randomGaussian() * 2
        #if random(1) < 0.5:
        #    self.speed.x = -1
        #else:
        #    self.speed.x = 1
        #    
        #if random(1) < 0.5:
        #    self.speed.y = -1
        #else:
        #    self.speed.y = 1
        
        self.pos = self.pos + self.speed

        self.fix_position()
        
    
        
    def fix_position(self):
        if self.pos.x > width:
            self.pos.x = self.pos.x - width
        if self.pos.x < 0:
            self.pos.x = width - self.pos.x
        if self.pos.y > height:
            self.pos.y = self.pos.y - height
        if self.pos.y < 0:
            self.pos.y = height - self.pos.y
