from controller import Controller

def setup():
    global controller
    controller = Controller()
    
def draw():
    global controller
    controller.draw()
    
def mouseClicked():
    global controller
    controller.add_mousefollower()

