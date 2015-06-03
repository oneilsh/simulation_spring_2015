import random as randommodule
from individual import Individual

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
    
    def individual_to_fitness(self, ind):
        return ind.fitness()    
    
    def cull(self):
        #self.individuals.sort(key = self.individual_to_fitness)
        self.individuals.sort()
        self.individuals = self.individuals[0:self.popsize]
        
    def print_fitness_stats(self):
        fitnesses = list()
        sum = 0.0
        for ind in self.individuals:
            fitnesses.append(ind.fitness())
            sum = sum + ind.fitness()
            
        meanfit = sum / len(self.individuals)
        fitnesses.sort()
        minfit = fitnesses[0]
        maxfit = fitnesses[len(fitnesses) - 1]
        medianfit = fitnesses[int(len(fitnesses)/2)]
        print("%s\t%s\t%s\t%s"%(minfit, meanfit, medianfit, maxfit))
        
        self.individuals.sort()
        bestind = self.individuals[0]
        bestind.debug_print()
        
        
