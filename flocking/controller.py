from agent import Agent
from mousefollower import MouseFollower
import voronoi

class Controller:
    def __init__(self):
        size(800, 600)
    
        self.agents = list()
        for i in range(0,40):
            newagent = Agent(PVector(random(0, width), random(0, height)),          # pos
                             PVector(random(0,0), random(0,0)), # speed
                             random(4,4.1),                         # maxspeed
                             random(0.1, 0.15),                   # maxforce
                             random(90, 90))                    # sightdist
            self.agents.append(newagent)

        ## grid for faster simulations
        self.gridsize = 100
        self.numrows = int(height/self.gridsize)
        self.numcols = int(width/self.gridsize)
        self.grid = list()
        for i in range(0, self.numrows):
            self.grid.append(list())
            for j in range(0, self.numcols):
                self.grid[i].append(list())



    def add_mousefollower(self):
            newagent = MouseFollower(PVector(mouseX, mouseY),          # pos
                                     PVector(random(-3,3), random(-3,3)), # speed
                                     random(2,2.1),                         # maxspeed
                                     random(0.1, 0.15),                   # maxforce
                                     random(200, 200))                    # sightdist
            self.agents.append(newagent)



    def draw(self):
        background(0, 0, 0)
        
        # clear grid lists
        for i in range(0, self.numrows):
            for j in range(0, self.numcols):
                #self.grid[i][j] = list()
                del self.grid[i][j][:]
        
        # register agents in grid
        for agent in self.agents:
            row = int(agent.pos.y/self.gridsize)
            col = int(agent.pos.x/self.gridsize)
            self.grid[row][col].append(agent)
            
        agent_positions = list()

        for agent in self.agents:
            agent_positions.append(agent.pos)

            agent.draw()
            
            nearby = list()
            row = int(agent.pos.y/self.gridsize)
            col = int(agent.pos.x/self.gridsize)
            nearby.extend(self.grid[row % self.numrows-1][col % self.numcols-1])
            nearby.extend(self.grid[row+1 % self.numrows-1][col+1 % self.numcols-1])
            nearby.extend(self.grid[row+1 % self.numrows-1][col % self.numcols-1])
            nearby.extend(self.grid[row % self.numrows-1][col+1 % self.numcols-1])
            nearby.extend(self.grid[row-1 % self.numrows-1][col-1 % self.numcols-1])
            nearby.extend(self.grid[row-1 % self.numrows-1][col % self.numcols-1])
            nearby.extend(self.grid[row % self.numrows-1][col-1 % self.numcols-1])
            nearby.extend(self.grid[row+1 % self.numrows-1][col-1 % self.numcols-1])
            nearby.extend(self.grid[row-1 % self.numrows-1][col+1 % self.numcols-1])

            if mousePressed:
                target = PVector(mouseX, mouseY)
                agent.seek(target)

            agent.cognate(nearby)
            
            agent.move()
            agent.reset_acceleration() # whoops
            
        v = voronoi.computeVoronoiDiagram(agent_positions)
        lines = v[1]
        vertices = v[0]
        stroke(255, 255, 255)
        for l in lines:
            v1index = l[1]
            v2index = l[2]
            if v1index != -1 and v2index != -1:
                p1 = vertices[v1index]
                p2 = vertices[v2index]
                line(p1[0], p1[1], p2[0], p2[1])
