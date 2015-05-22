class Agent:
    def __init__(self, initialpos, initialspeed, maxs, maxf):
        self.pos = initialpos
        self.speed = initialspeed
        self.acceleration = PVector(0, 0)
        self.mass = 1.0
        self.maxspeed = maxs
        self.maxforce = maxf
    
    def apply_force(self, force):
        self.acceleration = self.acceleration + force/self.mass
        
    def reset_acceleration(self):
        self.acceleration = self.acceleration * 0
    
    # donut-shaped world
    def fix_position(self):
        if self.pos.x > width:
            self.pos.x = self.pos.x - width
        elif self.pos.x < 0:
            self.pos.x = width - self.pos.x
        if self.pos.y > height:
            self.pos.y = self.pos.y - height
        elif self.pos.y < 0:
            self.pos.y = height - self.pos.y
            
    def seek(self, target):
        desired = target - self.pos
        distance = desired.mag() # for later
        desired.normalize()
        desired = desired * self.maxspeed
        
        if distance < 50:
            desired = desired * (distance/50)
            
        force = desired - self.speed
        force.limit(self.maxforce)
        self.apply_force(force)
        
            
    def move(self):
        self.speed = self.speed + self.acceleration
        self.speed.limit(self.maxspeed)
        self.pos = self.pos + self.speed
        self.fix_position()
        
    def draw(self):
        fill(40, 40, 40)
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
