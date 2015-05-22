from agent import Agent

class Controller:
    def __init__(self):
        size(800, 600)
        self.agents = list()
        for i in range(0,10):
            newagent = Agent(PVector(width/2, height/2),          # pos
                             PVector(random(-3,3), random(-3,3)), # speed
                             random(2,2.1),                         # maxspeed
                             random(0.1, 0.15))                   # maxforce
            self.agents.append(newagent)

    def draw(self):
        background(0, 0, 0)
        for agent in self.agents:
            agent.draw()

            if mousePressed:
                target = PVector(mouseX, mouseY)
                agent.seek(target)
            
            agent.move()
            agent.reset_acceleration() # whoops
