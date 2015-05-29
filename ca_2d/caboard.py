from cell import Cell
import sys

class CaBoard:
    def __init__(self, numrows, numcols):
        self.numrows = numrows
        self.numcols = numcols
        self.gen_number = 0
        self.currentgen = self.new_cell_list()
        self.lastgen = self.new_cell_list()
        
        #middle_cell = self.currentgen[int(self.numcells/2)]
        #middle_cell.set_state#(1)
        for row in range(0, self.numrows):
            for col in range(0, self.numcols):
                thecell = self.currentgen[row][col]
                if random(0,1) < 0.1:
                    thecell.set_state(1)
    
    def update(self):
        temp = self.lastgen
        self.lastgen = self.currentgen
        self.currentgen = temp
        self.gen_number = self.gen_number + 1
        neighborhood = [0, 0, 0, 0, 0, 0, 0, 0]  # new list of length 8 
        
        for row in range(0, self.numrows):
            for col in range(0, self.numcols):
                cell = self.lastgen[row][col]
                row = cell.row
                col = cell.col
                #neighborhood = [0, 0, 0]  
                neighborhood[0] = self.lastgen[(row - 1) % self.numrows][(col - 1) % self.numcols]
                neighborhood[1] = self.lastgen[row % self.numrows][(col - 1) % self.numcols]
                neighborhood[2] = self.lastgen[(row + 1) % self.numrows][(col - 1) % self.numcols]
                neighborhood[3] = self.lastgen[(row - 1) % self.numrows][(col + 1) % self.numcols]
                neighborhood[4] = self.lastgen[row % self.numrows][(col + 1) % self.numcols]
                neighborhood[5] = self.lastgen[(row + 1) % self.numrows][(col + 1) % self.numcols]
                neighborhood[6] = self.lastgen[(row - 1) % self.numrows][col % self.numcols]
                neighborhood[7] = self.lastgen[(row + 1) % self.numrows][col % self.numcols]
    
    
                nextstate = cell.compute_next_state(neighborhood)  # TODO
                
                self.currentgen[row][col].set_state(nextstate)
                
    def change_state(self, x, y):
        cellwidth = width/self.numcols
        cellheight = height/self.numrows
        row = int(y/cellheight)
        col = int(x/cellwidth)
        cell = self.currentgen[row][col]
        if cell.state == 1:
            cell.set_state(0)
        else:
            cell.set_state(1)
        
    def new_cell_list(self):
        cells = list()
        for row in range(0, self.numrows): # row
            newrow = list()
            for col in range(0, self.numcols): # col
                newrow.append(Cell(0, row, col))
            cells.append(newrow)
        return cells
    

    def draw(self):
        cellwidth = float(width)/self.numcols
        cellheight = float(height)/self.numrows
        for row in range(0, self.numrows):
            for col in range(0, self.numcols):
                cell = self.currentgen[row][col]
                cell.draw(cellwidth, cellheight) ## TODO
