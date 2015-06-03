import sys

class Individual:
    def __init__(self, coins_list, target):
        self.coins_list = coins_list
        self.target = target
        self.numcoins = len(coins_list)
        self.genotype = list()
        
        for i in range(0, self.numcoins):
            if random(0, 1) < 0.5:
                self.genotype.append(0)
            else:
                self.genotype.append(1)
                
    def debug_print(self):
        for i in range(0, self.numcoins):
            sys.stdout.write(self.genotype[i])
        sys.stdout.write("\n")
        
    def fitness(self):
        sum = 0.0
        for i in range(0, self.numcoins):
            sum = sum + self.genotype[i] * self.coins_list[i]
            
        return abs(sum - self.target)
    
    def mate_with(self, other):
        offspring = Individual(self.coins_list, self.target) # new random individual object
        
        crossover = int(random(0, self.numcoins))
        for i in range(0, crossover):
            offspring.genotype[i] = self.genotype[i]
        for i in range(crossover, self.numcoins):
            offspring.genotype[i] = other.genotype[i]
            
        return offspring
    

    def mutate(self):
        randlocus = int(random(0, self.numcoins))
        if self.genotype[randlocus] == 1:
            self.genotype[randlocus] = 0
        else:
            self.genotype[randlocus] = 1
            
    def __cmp__(self, other):
        if self.fitness() < other.fitness():
            return -1
        elif self.fitness() > other.fitness():
            return 1
        else:
            return 0

