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

#
# Make the is_on_board() function here that can get called by all of the classes
# @param moves, a list of all possible moves,
# this function returns the moves that are on the board and does not modify the original possible moves variable
# def is_on_board(moves):
#
#


class King:

    def __init__(self, team, location):
        self.location = location
        self.team = team

    def possible_moves(self):
        self.possible_moves = []
        self.possible_moves.append((self.location[0] + 1, self.location[1] + 1))
        self.possible_moves.append((self.location[0] + 1, self.location[1] + 0))
        self.possible_moves.append((self.location[0] + 1, self.location[1] - 1))
        self.possible_moves.append((self.location[0] + 0, self.location[1] + 1))
        self.possible_moves.append((self.location[0] + 0, self.location[1] - 1))
        self.possible_moves.append((self.location[0] - 1, self.location[1] + 1))
        self.possible_moves.append((self.location[0] - 1, self.location[1] + 0))
        self.possible_moves.append((self.location[0] - 1, self.location[1] - 1))

        self.possible_moves = is_on_board(self.possible_moves)

        self.possible_moves.sort(reverse=False)

        return self.possible_moves

    def legal_moves(self):
        self.legal_moves = []
        possible_moves = self.possible_moves()

        for i in range(len(possible_moves)):
            if square_is_open(self.team, possible_moves[i]) and path_is_clear(self.location, possible_moves[i]):
                self.legal_moves.append(possible_moves[i])

        return self.legal_moves


class Queen:

    def __init__(self, team, location):
        self.location = location
        self.team = team

    def possible_moves(self):
        self.possible_moves = []
        for i in range(1, 9):
            self.possible_moves.append((self.location[0] + i, self.location[1] + i))
            self.possible_moves.append((self.location[0] + i, self.location[1] - i))
            self.possible_moves.append((self.location[0] - i, self.location[1] + i))
            self.possible_moves.append((self.location[0] - i, self.location[1] - i))
            self.possible_moves.append((self.location[0] + i, self.location[1] + 0))
            self.possible_moves.append((self.location[0] - i, self.location[1] + 0))
            self.possible_moves.append((self.location[0] + 0, self.location[1] + i))
            self.possible_moves.append((self.location[0] + 0, self.location[1] - i))

        self.possible_moves = is_on_board(self.possible_moves)

        return self.possible_moves

    def legal_moves(self):
        self.legal_moves = []
        possible_moves = self.possible_moves()

        for i in range(len(possible_moves)):
            if square_is_open(self.team, possible_moves[i]) and path_is_clear(self.location, possible_moves[i]):
                self.legal_moves.append(possible_moves[i])

        return self.legal_moves


class Knight:

    def __init__(self, team, location):
        self.location = location
        self.team = team

    def possible_moves(self):
        self.possible_moves = []
        self.possible_moves.append((self.location[0] + 1, self.location[1] + 2))
        self.possible_moves.append((self.location[0] + 1, self.location[1] - 2))
        self.possible_moves.append((self.location[0] - 1, self.location[1] + 2))
        self.possible_moves.append((self.location[0] - 1, self.location[1] - 2))
        self.possible_moves.append((self.location[0] + 2, self.location[1] + 1))
        self.possible_moves.append((self.location[0] + 2, self.location[1] - 1))
        self.possible_moves.append((self.location[0] - 2, self.location[1] + 1))
        self.possible_moves.append((self.location[0] - 2, self.location[1] - 1))

        self.possible_moves = is_on_board(self.possible_moves)

        self.possible_moves.sort(reverse=False)

        return self.possible_moves

    def legal_moves(self):
        self.legal_moves = []
        possible_moves = self.possible_moves()

        for i in range(len(possible_moves)):
            if square_is_open(self.team, possible_moves[i]):
                self.legal_moves.append(possible_moves[i])

        return self.legal_moves


class Rook:

    def __init__(self, team, location):
        self.location = location
        self.team = team

    def possible_moves(self):
        self.possible_moves = []
        for i in range(1, 9):
            self.possible_moves.append((self.location[0] + i, self.location[1]))
            self.possible_moves.append((self.location[0] - i, self.location[1]))
            self.possible_moves.append((self.location[0], self.location[1] + i))
            self.possible_moves.append((self.location[0], self.location[1] - i))

        self.possible_moves = is_on_board(self.possible_moves)

        self.possible_moves.sort(reverse=False)

        return self.possible_moves

    def legal_moves(self):
        self.legal_moves = []
        possible_moves = self.possible_moves()

        for i in range(len(possible_moves)):
            if square_is_open(self.team, possible_moves[i]) and path_is_clear(self.location, possible_moves[i]):
                self.legal_moves.append(possible_moves[i])

        return self.legal_moves


class Bishop:

    def __init__(self, team, location):
        self.location = location
        self.team = team

    def possible_moves(self):
        self.possible_moves = []
        for i in range(1, 9):
            self.possible_moves.append((self.location[0] + i, self.location[1] + i))
            self.possible_moves.append((self.location[0] + i, self.location[1] - i))
            self.possible_moves.append((self.location[0] - i, self.location[1] + i))
            self.possible_moves.append((self.location[0] - i, self.location[1] - i))

        self.possible_moves = is_on_board(self.possible_moves)

        return self.possible_moves

    def legal_moves(self):
        self.legal_moves = []
        possible_moves = self.possible_moves()

        for i in range(len(possible_moves)):
            if square_is_open(self.team, possible_moves[i]) and path_is_clear(self.location, possible_moves[i]):
                self.legal_moves.append(possible_moves[i])

        return self.legal_moves


class Pawn:

    def __init__(self, team, location):
        self.location = location
        self.team = team

    def possible_moves(self):
        self.possible_moves = []
        team = self.team

        if team == "white":
            self.possible_moves.append((self.location[0] + 1, self.location[1] + 0))
            self.possible_moves.append((self.location[0] + 2, self.location[1] + 0))
            self.possible_moves.append((self.location[0] + 1, self.location[1] - 1))
            self.possible_moves.append((self.location[0] + 1, self.location[1] + 1))

        elif team == "black":
            self.possible_moves.append((self.location[0] - 1, self.location[1] + 0))
            self.possible_moves.append((self.location[0] - 2, self.location[1] + 0))
            self.possible_moves.append((self.location[0] - 1, self.location[1] - 1))
            self.possible_moves.append((self.location[0] - 1, self.location[1] + 1))

        self.possible_moves = is_on_board(self.possible_moves)

        return self.possible_moves

    def is_on_starting_square(self):
        is_on_starting_square = False
        team = self.team

        if team == "white":
            if self.location[0] == 1:
                is_on_starting_square = True

        if team == "black":
            if self.location[0] == 6:
                is_on_starting_square = True

        return is_on_starting_square

    def legal_moves(self):
        self.legal_moves = []
        possible_moves = self.possible_moves()
        is_on_starting_square = self.is_on_starting_square()

        if is_on_starting_square and path_is_clear(self.location, possible_moves[1]):
            self.legal_moves.append(possible_moves[1])

        possible_moves.pop(1)

        for i in range(len(possible_moves)):
            if square_is_open(self.team, possible_moves[i]) and path_is_clear(self.location, possible_moves[i]):
                self.legal_moves.append(possible_moves[i])

        return self.legal_moves


white_rook1 = Rook("white", (0, 0))
white_knight1 = Knight("white", (0, 1))
white_bishop1 = Bishop("white", (0, 2))
white_queen = Queen("white", (0, 3))
white_king = King("white", (0, 4))
white_bishop2 = Bishop("white", (0, 5))
white_knight2 = Knight("white", (0, 6))
white_rook2 = Rook("white", (0, 7))

white_pawn0 = Pawn("white", (1, 0))
white_pawn1 = Pawn("white", (1w, 0))
white_pawn2 = Pawn("white", (1, 2))
white_pawn3 = Pawn("white", (1, 3))
white_pawn4 = Pawn("white", (1, 4))
white_pawn5 = Pawn("white", (1, 5))
white_pawn6 = Pawn("white", (1, 6))
white_pawn7 = Pawn("white", (1, 7))

black_rook1 = Rook("black", (7, 0))
black_knight1 = Rook("black", (7, 1))
black_bishop1 = Rook("black", (7, 2))
black_queen = Rook("black", (7, 3))
black_king = Rook("black", (7, 4))
black_bishop2 = Rook("black", (7, 5))
black_knight2 = Rook("black", (7, 6))
black_rook2 = Rook("black", (7, 7))

black_pawn0 = Pawn("black", (6, 0))
black_pawn1 = Pawn("black", (6, 1))
black_pawn2 = Pawn("black", (6, 2))
black_pawn3 = Pawn("black", (6, 3))
black_pawn4 = Pawn("black", (6, 4))
black_pawn5 = Pawn("black", (6, 5))
black_pawn6 = Pawn("black", (6, 6))
black_pawn7 = Pawn("black", (6, 7))


def square_is_open(team, location):
    def white_squares_occupied():
        white_squares_occupied = []
        white_squares_occupied.append(white_rook1.location)
        white_squares_occupied.append(white_rook2.location)
        white_squares_occupied.append(white_knight1.location)
        white_squares_occupied.append(white_knight2.location)
        white_squares_occupied.append(white_bishop1.location)
        white_squares_occupied.append(white_bishop2.location)
        white_squares_occupied.append(white_queen.location)
        white_squares_occupied.append(white_king.location)
        white_squares_occupied.append(white_pawn0.location)
        white_squares_occupied.append(white_pawn1.location)
        white_squares_occupied.append(white_pawn2.location)
        white_squares_occupied.append(white_pawn3.location)
        white_squares_occupied.append(white_pawn4.location)
        white_squares_occupied.append(white_pawn5.location)
        white_squares_occupied.append(white_pawn6.location)
        white_squares_occupied.append(white_pawn7.location)
        return white_squares_occupied

    def black_squares_occupied():
        black_squares_occupied = []
        black_squares_occupied.append(black_rook1.location)
        black_squares_occupied.append(black_rook2.location)
        black_squares_occupied.append(black_knight1.location)
        black_squares_occupied.append(black_knight2.location)
        black_squares_occupied.append(black_bishop1.location)
        black_squares_occupied.append(black_bishop2.location)
        black_squares_occupied.append(black_queen.location)
        black_squares_occupied.append(black_king.location)
        black_squares_occupied.append(black_pawn0.location)
        black_squares_occupied.append(black_pawn1.location)
        black_squares_occupied.append(black_pawn2.location)
        black_squares_occupied.append(black_pawn3.location)
        black_squares_occupied.append(black_pawn4.location)
        black_squares_occupied.append(black_pawn5.location)
        black_squares_occupied.append(black_pawn6.location)
        black_squares_occupied.append(black_pawn7.location)
        return black_squares_occupied

    square_is_open = True
    if team == "white":
        if location in white_squares_occupied():
            square_is_open = False

    if team == "black":
        if location in black_squares_occupied():
            square_is_open = False

    if team == "both":
        if location in white_squares_occupied() or location in black_squares_occupied():
            square_is_open = False

    return square_is_open


def is_on_board(possible_moves):
    while possible_moves:
        all_good = True
        for i in range(len(possible_moves)):
            if possible_moves[i][0] < 0 or possible_moves[i][1] < 0 or possible_moves[i][0] > 7 or possible_moves[i][
                1] > 7:
                possible_moves.pop(i)
                all_good = False
                break

        if all_good:
            break

    return possible_moves


def path_is_clear(starting_location, ending_location):
    path_is_clear = True

    for i in range(1, 9):

        if starting_location[0] + i == ending_location[0] and starting_location[1] == ending_location[1]:

            intermediate_location = (starting_location[0] + 1, starting_location[1])

            while intermediate_location[0] != ending_location[0]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0] + 1, intermediate_location[1])
                intermediate_location = intermediate_location1

            if intermediate_location[0] == ending_location[0]:
                if not square_is_open("both", (intermediate_location[0], intermediate_location[1])):
                    path_is_clear = False

            break

        elif starting_location[0] - i == ending_location[0] and starting_location[1] == ending_location[1]:

            intermediate_location = (starting_location[0] - 1, starting_location[1])

            while intermediate_location[0] != ending_location[0]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0] - 1, intermediate_location[1])
                intermediate_location = intermediate_location1

            if intermediate_location[0] == ending_location[0]:
                if not square_is_open("both", (intermediate_location[0], intermediate_location[1])):
                    path_is_clear = False

            break

        elif starting_location[0] == ending_location[0] and starting_location[1] + 1 == ending_location[1]:

            intermediate_location = (starting_location[0], starting_location[1] + 1)

            while intermediate_location[1] != ending_location[1]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0], intermediate_location[1] + 1)
                intermediate_location = intermediate_location1

            if intermediate_location[0] == ending_location[0]:
                if not square_is_open("both", (intermediate_location[0], intermediate_location[1])):
                    path_is_clear = False

            break

        elif starting_location[0] == ending_location[0] and starting_location[1] - i == ending_location[1]:

            intermediate_location = (starting_location[0], starting_location[1] - 1)

            while intermediate_location[1] != ending_location[1]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0], intermediate_location[1] - 1)
                intermediate_location = intermediate_location1

            if intermediate_location[0] == ending_location[0]:
                if not square_is_open("both", (intermediate_location[0], intermediate_location[1])):
                    path_is_clear = False

            break

        elif starting_location[0] + i == ending_location[0] and starting_location[1] + i == ending_location[1]:

            intermediate_location = (starting_location[0] + 1, starting_location[1] + 1)

            while intermediate_location[0] != ending_location[0] and intermediate_location[1] != ending_location[1]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0] + 1, intermediate_location[1] + 1)
                intermediate_location = intermediate_location1

            if intermediate_location[0] == ending_location[0]:
                if not square_is_open("both", (intermediate_location[0], intermediate_location[1])):
                    path_is_clear = False

            break

        elif starting_location[0] + i == ending_location[0] and starting_location[1] - i == ending_location[1]:

            intermediate_location = (starting_location[0] + 1, starting_location[1] - 1)

            while intermediate_location[0] != ending_location[0] and intermediate_location[1] != ending_location[1]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0] + 1, intermediate_location[1] - 1)
                intermediate_location = intermediate_location1

            if intermediate_location[0] == ending_location[0]:
                if not square_is_open("both", (intermediate_location[0], intermediate_location[1])):
                    path_is_clear = False

            break

        elif starting_location[0] - i == ending_location[0] and starting_location[1] + i == ending_location[1]:

            intermediate_location = (starting_location[0] - 1, starting_location[1] + 1)

            while intermediate_location[0] != ending_location[0] and intermediate_location[1] != ending_location[1]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0] - 1, intermediate_location[1] + 1)
                intermediate_location = intermediate_location1

            if intermediate_location[0] == ending_location[0]:
                if not square_is_open("both", (intermediate_location[0], intermediate_location[1])):
                    path_is_clear = False

            break

        elif starting_location[0] - i == ending_location[0] and starting_location[1] - i == ending_location[1]:

            intermediate_location = (starting_location[0] - 1, starting_location[1] - 1)

            while intermediate_location[0] != ending_location[0] and intermediate_location[1] != ending_location[1]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0] - 1, intermediate_location[1] - 1)
                intermediate_location = intermediate_location1

            if intermediate_location[0] == ending_location[0]:
                if not square_is_open("both", (intermediate_location[0], intermediate_location[1])):
                    path_is_clear = False

            break

    return path_is_clear




