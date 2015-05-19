class Agent:
    def __init__(self, initialpos, initialspeed, maxs):
        self.pos = initialpos
        self.speed = initialspeed
        self.acceleration = PVector(0, 0)
        self.mass = 1.0
        self.maxspeed = maxs
    
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
            
    def move(self):
        self.speed = self.speed + self.acceleration
        self.speed.limit(self.maxspeed)
        self.pos = self.pos + self.speed
        self.fix_position()
        
    def draw(self):
        fill(40, 40, 40)
        stroke(255, 255, 255)
        ellipse(self.pos.x, self.pos.y, 10, 10)

