'''
This program is a 2 player chess game written by Zach Dworkin, Evan Dworkin, and Matthew Dworkin
press the green check to commit changes, then shift+command+k to push them to github, then click push
to update master github branch

PLAN
Methods:
    Location (row,column) = (0-7, 0-7)
        create:
            is_legal_move(args)
            possible_moves(args)
    Pieces
        classes, dictionary, hard code?
    Team

Possibility for Pieces:
    create a separate class for each king of piece ex:

    class King:

        def __init__(location, self):
            self.location = location

        def possible_moves(self):#returns a list of possible move locations


'''

from graphics import *
from g_interface import *

class King:

    def __init__(location, self):
        self.location = location

    def possible_moves(self):#returns a list of possible move locations

