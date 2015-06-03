import random as randommodule

class Population:
    def __init__(self, coins_list, target, popsize):
        self.coins_list = coins_list
        self.target = target
        self.individuals = list()
        self.popsize = popsize
        for i in range(0, self.popsize):
            self.individuals.append(Individual(coins_list, target))
            
    
    def mate_random(self):
        for i in range(0, int(self.popsize/4)): # 25% mate rate
            pair = randommodule.sample(self.individuals, 2)
            offspring = pair[0].mate_with(pair[1])
            if random(0, 1) < 0.1:
                offspring.mutate()
                
            self.individuals.append(offspring)
            
        
