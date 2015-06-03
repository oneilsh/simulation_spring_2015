from population import Population
import time

class Controller:
    def __init__(self):
        self.coins_list = [0.25, 0.25, 0.1, 1, 5, 2, 5, 10, 0.1, 0.1, 0.01, 0.01, 0.01, 2, 1, 5, 0.1]
        self.target = 8.47
        self.population = Population(self.coins_list, self.target, 100)
        
    def draw(self):
        self.population.print_fitness_stats()
        self.population.mate_random()
        self.population.cull()
        time.sleep(0.2)
