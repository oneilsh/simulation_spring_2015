class Circle:
    def __init__(self, pos, d, speed):
        self.pos = pos
        self.speed = speed
        self.d = d
        
    def draw(self):
        fill(200, 50, 50)
        ellipse(self.pos.x, self.pos.y, self.d, self.d)
        
    def move(self):
        self.pos = self.pos + self.speed
        self.speed = self.speed * 1.01
        
        if self.pos.y + self.d/2.0 >= height or self.pos.y - self.d/2.0 <= 0:
            self.speed.y = self.speed.y * -1
            
        if self.pos.x + self.d/2.0 >= width or self.pos.x - self.d/2.0 <= 0:
            self.speed.x = self.speed.x * -1

