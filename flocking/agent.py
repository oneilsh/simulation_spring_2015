class Agent:
    def __init__(self, initialpos, initialspeed, maxs, maxf, sdist):
        self.pos = initialpos
        self.speed = initialspeed
        self.acceleration = PVector(0, 0)
        self.mass = 1.0
        self.maxspeed = maxs
        self.maxforce = maxf
        self.sightdistance = sdistz
    
    def apply_force(self, force):
        self.acceleration = self.acceleration + force/self.mass
        
    def reset_acceleration(self):
        self.acceleration = self.acceleration * 0
    
    # donut-shaped world
    def fix_position(self):
        if self.pos.x > width:
            self.pos.x = self.pos.x - width
        elif self.pos.x < 0:
            self.pos.x = width + self.pos.x
        if self.pos.y > height:
            self.pos.y = self.pos.y - height
        elif self.pos.y < 0:
            self.pos.y = height + self.pos.y
         
    
    def cognate(self, agents):
        neighbors = list()
        for agent in agents:
            if agent != self:
                diffvec = agent.pos - self.pos
                if diffvec.mag() < self.sightdistance:
                    neighbors.append(agent)

        self.flock(neighbors)
        
    def align_force(self, agents):
        sum = PVector(0, 0)
        for agent in agents:
            sum = sum + agent.speed
            
        desired = sum / len(agents)
        
        return self.desired_to_force(desired)
    
    def separate_force(self, agents):
        sum = PVector(0, 0)
        for agent in agents:
            flee = self.pos - agent.pos
            fleedist = flee.mag()
            flee.normalize()
            sum = sum + flee / (fleedist + 0.00001)    
            
        avgfleedesired = sum / len(agents)

        return self.desired_to_force(avgfleedesired)
    

    def cohesion_force(self, agents):
        sum = PVector(0, 0)
        for agent in agents:
            sum = sum + agent.pos
            
        avgpos = sum / len(agents)    
        desired = avgpos - self.pos
        
        return self.desired_to_force(desired)
    
    def desired_to_force(self, desired):
        desired_c = desired #.get()
        desired_c.normalize()
        desired_c = desired_c * self.maxspeed
        force = desired_c - self.speed
        force.limit(self.maxforce)
        return force
        
    def flock(self, agents):
        if len(agents) > 0:
            separate_force = self.separate_force(agents)
            self.apply_force(separate_force * 1.4)
            align_force = self.align_force(agents)
            self.apply_force(align_force)
            cohesion_force = self.cohesion_force(agents)
            self.apply_force(cohesion_force)
        
        
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
        
        rect(-10.0, -2.5, 20.0, 5.0)
        
        pushMatrix()  # whisker 1
        rotate(-1*PI/8)
        line(0.0, 0.0, 20.0, 0.0)
        popMatrix()
        
        pushMatrix()  # whisker 2
        rotate(PI/8)
        line(0.0, 0.0, 20.0, 0.0)
        popMatrix()
        
        popMatrix()
