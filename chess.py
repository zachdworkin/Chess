'''
This program is a 2 player chess game written by Zach Dworkin, Evan Dworkin, and Matthew Dworkin
press the green check to commit changes, then shift+command+k to push them to github, then click push
to update master github branch

PLAN
Methods:
    Location (row,column) = (0-7, 0-7)
        create:
            is_legal_move(args) = check if it is moving through an enemy, on your team, or empty spot, etc
            possible_moves(args) = all possible moves even if they are not legal (must be on board)
    Pieces
        classes, dictionary, hard code?
    Team

Possibility for Pieces:
    create a separate class for each king of piece ex:

    class King:

        def __init__(location, team, self):
            self.location = location
            self.team = team

        def possible_moves(self):#returns a list of possible move locations


'''

from graphics import *
from g_interface import *
