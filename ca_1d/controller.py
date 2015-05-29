from caboard import CaBoard
import time

class Controller:
    def __init__(self):
        size(600, 600)
        self.caboard = CaBoard(100)   # no of cells in the world
        
    def draw(self):
        self.caboard.draw()
        self.caboard.update()
        time.sleep(0.05)                # sleep 1 second
