from agent import Agent

class Controller:
    def __init__(self):
        size(600, 400)
        self.agents = list()
        for i in range(0,10):
            newagent = Agent(PVector(width/2, height/2),          # pos
                             PVector(random(-3,3), random(-3,3)), # speed
                             random(1,5))                         # maxspeed
            self.agents.append(newagent)
            
            
    def draw(self):
        background(0, 0, 0)
        for agent in self.agents:
            agent.move()
            agent.draw()
            
        agent.reset_acceleration()
