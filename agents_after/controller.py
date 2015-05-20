from agent import Agent

class Controller:
    def __init__(self):
        size(600, 400)
        self.agents = list()
        for i in range(0,10):
            newagent = Agent(PVector(width/2, height/2),          # pos
                             PVector(random(-3,3), random(-3,3)), # speed
                             random(1,5),                         # maxspeed
                             random(0.02, 0.2))                   # maxforce
            self.agents.append(newagent)
            
            
    def draw(self):
        background(0, 0, 0)
        for agent in self.agents:
            agent.draw()

            if mousePressed:
                target = PVector(mouseX, mouseY)
                agent.seek(target)
            
            agent.move()
            
            agent.reset_acceleration() # THIS WAS NOT INSIDE THE AGENT LOOP!
