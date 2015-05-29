from caboard import CaBoard
import time

class Controller:
    def __init__(self):
        size(600, 600)
        self.caboard = CaBoard(50, 50)   # no of cells in the world in x, and y
        self.updating = True
        

    
    def draw(self):
        self.caboard.draw()
        if self.updating:
            self.caboard.update()
        time.sleep(0.05)                # sleep 1 second
        
        if mousePressed:
            self.caboard.change_state(mouseX, mouseY)
        if keyPressed:
            self.updating = not self.updating
