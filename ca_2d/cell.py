
class Cell:
    def __init__(self, initstate, initrow, initcol):
        self.state = initstate
        self.row = initrow
        self.col = initcol
        
    def set_state(self, newstate):
        self.state = newstate
        
    def compute_next_state(self, nbh):
        count = 0
        for cell in nbh:
            if cell.state == 1:
                count = count + 1
        
        if self.state == 1 and count < 2:
            return 0
        if self.state == 1 and count > 3:
            return 0
        if self.state == 0 and count == 3:
            return 1
        return self.state
                
        
    def draw(self, cellwidth, cellheight):
        stroke(0, 0, 0)
        if self.state == 1:
            fill(200, 200, 200)
        else:
            fill(40, 40, 40)
            
        posx = self.col * cellwidth
        posy = self.row * cellheight
        rect(posx, posy, cellwidth, cellheight)
