class Circle:
    def __init__(self, pos, d, speed):
        self.pos = pos
        self.speed = speed
        self.d = d
        self.mass = d/50 # mass scales with diameter
        self.acceleration = PVector(0, 0)
        
    def apply_force(self, force):
        # F = MA
        self.acceleration = self.acceleration + force/self.mass
        
    def draw(self):
        fill(200, 50, 50)
        ellipse(self.pos.x, self.pos.y, self.d, self.d)

    def reset_acceleration(self):
        self.acceleration = self.acceleration * 0

    def bounce_and_fix(self):
        # bounce
        if self.pos.y + self.d/2.0 >= height or self.pos.y - self.d/2.0 <= 0:
            self.speed.y = self.speed.y * -1.0
            
        if self.pos.x + self.d/2.0 >= width or self.pos.x - self.d/2.0 <= 0:
            self.speed.x = self.speed.x * -1.0
            
        ##if the circle is still outside the bounds, move it back in
        ##(to avoid it getting "stuck")
        if self.pos.y + self.d/2 > height:
            self.pos.y = height - self.d/2
        if self.pos.y - self.d/2 < 0:
            self.pos.y = self.d/2
        if self.pos.x + self.d/2 > width:
            self.pos.x = width - self.d/2
        if self.pos.x - self.d/2 < 0:
            self.pos.x = self.d/2


    def move(self, circles):
        # acceleration: change in speed over time
        self.speed = self.speed + self.acceleration
        self.speed.limit(10)
        # speed: change in position over time
        self.pos = self.pos + self.speed
        self.bounce_and_fix()
                    

