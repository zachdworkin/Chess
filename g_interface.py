from graphics import *
from chess import *

win = GraphWin()
def create_board(state):
    cir = Circle(Point(100,50), 25)
    cir.draw(win)
    win.getMouse()
    return 0

create_board(1)
win.close()