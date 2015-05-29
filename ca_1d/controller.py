from caboard import CaBoard
import time

class Controller:
    def __init__(self):
        self.caboard = CaBoard(50)   # no of cells in the world
        
    def draw(self):
        self.caboard.draw()
        self.caboard.update()
        time.sleep(1)                # sleep 1 second
