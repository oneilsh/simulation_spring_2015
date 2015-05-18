from particle import Particle

class Controller:
    def __init__(self):
        size(600, 400)
        self.particles = list()
        for i in range(0,200):
            newparticle = Particle(PVector(width/4, height/4))
            self.particles.append(newparticle)
            
    def draw(self):
        #background(0,0,0)
        fill(0, 0, 0, 20)   # red, green, blue, alpha: 0 to 255
        rect(0, 0, width, height)
        for particle in self.particles:
            particle.draw()
            particle.move()            

        print(self.entropy_quadrants())
                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                        
    def entropy_quadrants(self):
        total = len(self.particles)
        counts = [0, 0, 0, 0] # ul, ur, ll, lr quandrants
        
        for particle in self.particles:
            if particle.pos.x < width/2:
                if particle.pos.y < height/2:
                    counts[0] = counts[0] + 1
                else:
                    counts[2] = counts[2] + 1
            else:
                if particle.pos.y < height/2:
                    counts[1] = counts[1] + 1
                else:
                    counts[3] = counts[3] + 1
                    
        entropy = 0.0
        for count in counts:
            prob = count/float(total)
            if prob > 0:
                entropy = entropy + -1 * prob * log(prob)/log(2.0)
        
        return entropy
