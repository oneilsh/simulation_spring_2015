
class Cell:
    def __init__(self, initstate, initpos):
        self.state = initstate
        self.position = initpos
        
    def set_state(self, newstate):
        self.state = newstate
        
    def compute_next_state(self, nbh):
        if nbh[0].state == 1 and nbh[1].state == 1 and nbh[2].state == 1:
            return 0
        elif nbh[0].state == 1 and nbh[1].state == 1 and nbh[2].state == 0:
            return 0
        elif nbh[0].state == 1 and nbh[1].state == 0 and nbh[2].state == 1:
            return 0
        elif nbh[0].state == 1 and nbh[1].state == 0 and nbh[2].state == 0:
            return 1
        elif nbh[0].state == 0 and nbh[1].state == 1 and nbh[2].state == 1:
            return 1
        elif nbh[0].state == 0 and nbh[1].state == 1 and nbh[2].state == 0:
            return 1
        elif nbh[0].state == 0 and nbh[1].state == 0 and nbh[2].state == 1:
            return 1
        elif nbh[0].state == 0 and nbh[1].state == 0 and nbh[2].state == 0:
            return 0
        else:
            print("wft")
