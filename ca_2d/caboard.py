from cell import Cell
import sys

class CaBoard:
    def __init__(self, numrows, numcols):
        self.numrows = numrows
        self.numcols = numcols
        self.gen_number = 0
        self.currentgen = self.new_cell_list()
        self.lastgen = self.new_cell_list()
        
        for rownum in range(0, self.numrows):
            for colnum in range(0, self.numcols):
                cell = self.currentgen[rownum][colnum]
                if random(0,1) < 0.1:
                    cell.set_state(1)
        
    def change_state(self, x, y):
        cellwidth = width/self.numcols
        cellheight = height/self.numrows
        
        row = int(y/cellwidth)
        col = int(x/cellheight)
        cell = self.currentgen[row][col]
        if cell.state == 1:
            cell.set_state(0)
        else:
            cell.set_state(1)
        
    def update(self):
        temp = self.lastgen
        self.lastgen = self.currentgen
        self.currentgen = temp
        self.gen_number = self.gen_number + 1
        neighborhood = [0, 0, 0, 0, 0, 0, 0, 0]  # new list of length 3 
        
        for rownum in range(0, self.numrows):
            for colnum in range(0, self.numcols):
                cell = self.lastgen[rownum][colnum]
                row = cell.row
                col = cell.col
                
                neighborhood[0] = self.lastgen[(row - 1) % self.numrows][(col - 1) % self.numcols]
                neighborhood[1] = self.lastgen[row % self.numrows][(col - 1) % self.numcols]
                neighborhood[2] = self.lastgen[(row + 1) % self.numrows][(col - 1) % self.numcols]
                neighborhood[3] = self.lastgen[(row - 1) % self.numrows][(col + 1) % self.numcols]
                neighborhood[4] = self.lastgen[row % self.numrows][(col + 1) % self.numcols]
                neighborhood[5] = self.lastgen[(row + 1) % self.numrows][(col + 1) % self.numcols]
                neighborhood[6] = self.lastgen[(row - 1) % self.numrows][(col) % self.numcols]
                neighborhood[7] = self.lastgen[(row + 1) % self.numrows][(col) % self.numcols]

                nextstate = cell.compute_next_state(neighborhood)  # TODO

                self.currentgen[row][col].set_state(nextstate)
            
        
    def new_cell_list(self):
        cells = list()
        for rownum in range(0, self.numrows):
            newrow = list()
            for colnum in range(0, self.numcols):
                cell = Cell(0, rownum, colnum)
                newrow.append(cell)
            cells.append(newrow)
        return cells
    

    def draw(self):
        ## todo: fixup
        stroke(0, 0, 0)
        cellheight = height/float(self.numrows)
        cellwidth = width/float(self.numcols)
        
        
        for rownum in range(0, self.numrows):
            for colnum in range(0, self.numcols):
                cell = self.currentgen[rownum][colnum]
        
                cell.draw(cellwidth, cellheight)
