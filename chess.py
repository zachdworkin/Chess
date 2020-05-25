'''
This program is a 2 player chess game written by Zach Dworkin, Evan Dworkin, and Matthew Dworkin
press the green check to commit changes, then shift+command+k to push them to github, then click push
to update master github branch
'''


from graphics import *
from g_interface import *

win = GraphWin()
def create_board(state):
    cir = Circle(Point(100,50), 25)
    cir.draw(win)
    win.getMouse()
    return 0

create_board(1)
win.close()
