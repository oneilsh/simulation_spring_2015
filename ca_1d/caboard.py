from cell import Cell
import sys

class CaBoard:
    def __init__(self, numcells):
        self.numcells = numcells
        self.gen_number = 0
        self.currentgen = self.new_cell_list()
        self.lastgen = self.new_cell_list()
        
        #middle_cell = self.currentgen[int(self.numcells/2)]
        #middle_cell.set_state#(1)
        for cell in self.currentgen:
            if random(0,1) < 0.2:
                cell.set_state(1)
    
    def update(self):
        temp = self.lastgen
        self.lastgen = self.currentgen
        self.currentgen = temp
        self.gen_number = self.gen_number + 1
        neighborhood = [0, 0, 0]  # new list of length 3 
        
        for cell in self.lastgen:
            pos = cell.position
            #neighborhood = [0, 0, 0]  
            neighborhood[0] = self.lastgen[(pos - 1) % self.numcells]
            neighborhood[1] = self.lastgen[pos % self.numcells]
            neighborhood[2] = self.lastgen[(pos + 1) % self.numcells]

            nextstate = cell.compute_next_state(neighborhood)  # TODO
            
            self.currentgen[pos].set_state(nextstate)
            
        
    def new_cell_list(self):
        cells = list()
        for i in range(0, self.numcells):
            cells.append(Cell(0, i))
        return cells
    

    def draw(self):
        for cell in self.currentgen:
            if cell.state == 1:
                sys.stdout.write("#")
            else:
                sys.stdout.write(" ")
        sys.stdout.write("\n")
