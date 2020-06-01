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

    def is_check(self):
        is_check = False
        location = self.location
        team = self.team

        if team == "white":
            if location in black_moveable_squares():
                is_check = True

        if team == "black":
            if location in white_moveable_squares():
                is_check = True

        return is_check


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

        if self.team == "white":
            if self.location[0] == 1:
                is_on_starting_square = True

        if self.team == "black":
            if self.location[0] == 6:
                is_on_starting_square = True

        return is_on_starting_square

    def can_attack_diagonally(self, starting_location, ending_location):
        can_attack_diagonally = False

        if self.team == "white":
            if ending_location[0] == starting_location[0] + 1 and ending_location[1] == starting_location[
                1] + 1 and enemy_occupies_square("white", ending_location):
                can_attack_diagonally = True
            elif ending_location[0] == starting_location[0] + 1 and ending_location[1] == starting_location[
                1] - 1 and enemy_occupies_square("white", ending_location):
                can_attack_diagonally = True

        if self.team == "black":
            if ending_location[0] == starting_location[0] - 1 and ending_location[1] == starting_location[
                1] + 1 and enemy_occupies_square("black", ending_location):
                can_attack_diagonally = True
            elif ending_location[0] == starting_location[0] - 1 and ending_location[1] == starting_location[
                1] - 1 and enemy_occupies_square("black", ending_location):
                can_attack_diagonally = True

        return can_attack_diagonally

    def legal_moves(self):
        self.legal_moves = []
        possible_moves = self.possible_moves()

        if self.team == "white":
            if not enemy_occupies_square(self.team, ((possible_moves[0][0], possible_moves[0][1]))):
                self.legal_moves.append(possible_moves[0])
                if self.is_on_starting_square() and not enemy_occupies_square(self.team, (
                (possible_moves[1][0], possible_moves[1][1]))) and possible_moves[1][0] == self.location[0] + 2:
                    self.legal_moves.append(possible_moves[1])

        elif self.team == "black":
            if not enemy_occupies_square(self.team, ((possible_moves[0][0], possible_moves[0][1]))):
                self.legal_moves.append(possible_moves[0])
                if self.is_on_starting_square() and not enemy_occupies_square(self.team, (
                (possible_moves[1][0], possible_moves[1][1]))) and possible_moves[1][0] == self.location[0] - 2:
                    self.legal_moves.append(possible_moves[1])

        for i in range(len(possible_moves)):
            if self.can_attack_diagonally(self.location, possible_moves[i]):
                self.legal_moves.append(possible_moves[i])

        return self.legal_moves


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


def square_is_open(team, location):
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


def enemy_occupies_square(team, location):
    enemy_occupies_square = False
    if team == "black":
        if location in white_squares_occupied():
            enemy_occupies_square = True

    if team == "white":
        if location in black_squares_occupied():
            enemy_occupies_square = True

    return enemy_occupies_square


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

            break

        elif starting_location[0] - i == ending_location[0] and starting_location[1] == ending_location[1]:

            intermediate_location = (starting_location[0] - 1, starting_location[1])

            while intermediate_location[0] != ending_location[0]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0] - 1, intermediate_location[1])
                intermediate_location = intermediate_location1

            break

        elif starting_location[0] == ending_location[0] and starting_location[1] + 1 == ending_location[1]:

            intermediate_location = (starting_location[0], starting_location[1] + 1)

            while intermediate_location[1] != ending_location[1]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0], intermediate_location[1] + 1)
                intermediate_location = intermediate_location1

            break

        elif starting_location[0] == ending_location[0] and starting_location[1] - i == ending_location[1]:

            intermediate_location = (starting_location[0], starting_location[1] - 1)

            while intermediate_location[1] != ending_location[1]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0], intermediate_location[1] - 1)
                intermediate_location = intermediate_location1

            break

        elif starting_location[0] + i == ending_location[0] and starting_location[1] + i == ending_location[1]:

            intermediate_location = (starting_location[0] + 1, starting_location[1] + 1)

            while intermediate_location[0] != ending_location[0] and intermediate_location[1] != ending_location[1]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0] + 1, intermediate_location[1] + 1)
                intermediate_location = intermediate_location1

            break

        elif starting_location[0] + i == ending_location[0] and starting_location[1] - i == ending_location[1]:

            intermediate_location = (starting_location[0] + 1, starting_location[1] - 1)

            while intermediate_location[0] != ending_location[0] and intermediate_location[1] != ending_location[1]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0] + 1, intermediate_location[1] - 1)
                intermediate_location = intermediate_location1

            break

        elif starting_location[0] - i == ending_location[0] and starting_location[1] + i == ending_location[1]:

            intermediate_location = (starting_location[0] - 1, starting_location[1] + 1)

            while intermediate_location[0] != ending_location[0] and intermediate_location[1] != ending_location[1]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0] - 1, intermediate_location[1] + 1)
                intermediate_location = intermediate_location1

            break

        elif starting_location[0] - i == ending_location[0] and starting_location[1] - i == ending_location[1]:

            intermediate_location = (starting_location[0] - 1, starting_location[1] - 1)

            while intermediate_location[0] != ending_location[0] and intermediate_location[1] != ending_location[1]:

                if not square_is_open("both", intermediate_location):
                    path_is_clear = False
                    break

                intermediate_location1 = (intermediate_location[0] - 1, intermediate_location[1] - 1)
                intermediate_location = intermediate_location1

            break

    return path_is_clear


def white_moveable_squares():
    white_moveable_squares = []
    white_moveable_squares += white_rook1.legal_moves()
    white_moveable_squares += white_rook2.legal_moves()
    white_moveable_squares += white_knight1.legal_moves()
    white_moveable_squares += white_knight2.legal_moves()
    white_moveable_squares += white_bishop1.legal_moves()
    white_moveable_squares += white_bishop2.legal_moves()
    white_moveable_squares += white_queen.legal_moves()
    white_moveable_squares += white_king.legal_moves()
    white_moveable_squares += white_pawn0.legal_moves()
    white_moveable_squares += white_pawn1.legal_moves()
    white_moveable_squares += white_pawn2.legal_moves()
    white_moveable_squares += white_pawn3.legal_moves()
    white_moveable_squares += white_pawn4.legal_moves()
    white_moveable_squares += white_pawn5.legal_moves()
    white_moveable_squares += white_pawn6.legal_moves()
    white_moveable_squares += white_pawn7.legal_moves()

    white_moveable_squares_no_dupes = []
    for i in white_moveable_squares:
        if i not in white_moveable_squares_no_dupes:
            white_moveable_squares_no_dupes.append(i)

    return white_moveable_squares_no_dupes


def black_moveable_squares():
    black_moveable_squares = []
    black_moveable_squares += black_rook1.legal_moves()
    black_moveable_squares += black_rook2.legal_moves()
    black_moveable_squares += black_knight1.legal_moves()
    black_moveable_squares += black_knight2.legal_moves()
    black_moveable_squares += black_bishop1.legal_moves()
    black_moveable_squares += black_bishop2.legal_moves()
    black_moveable_squares += black_queen.legal_moves()
    black_moveable_squares += black_king.legal_moves()
    black_moveable_squares += black_pawn0.legal_moves()
    black_moveable_squares += black_pawn1.legal_moves()
    black_moveable_squares += black_pawn2.legal_moves()
    black_moveable_squares += black_pawn3.legal_moves()
    black_moveable_squares += black_pawn4.legal_moves()
    black_moveable_squares += black_pawn5.legal_moves()
    black_moveable_squares += black_pawn6.legal_moves()
    black_moveable_squares += black_pawn7.legal_moves()

    black_moveable_squares_no_dupes = []
    for i in black_moveable_squares:
        if i not in black_moveable_squares_no_dupes:
            black_moveable_squares_no_dupes.append(i)

    return black_moveable_squares_no_dupes


white_rook1 = Rook("white", (0, 0))
white_knight1 = Knight("white", (0, 1))
white_bishop1 = Bishop("white", (0, 2))
white_queen = Queen("white", (0, 3))
white_king = King("white", (0, 4))
white_bishop2 = Bishop("white", (0, 5))
white_knight2 = Knight("white", (0, 6))
white_rook2 = Rook("white", (0, 7))

white_pawn0 = Pawn("white", (1, 0))
white_pawn1 = Pawn("white", (1, 0))
white_pawn2 = Pawn("white", (1, 2))
white_pawn3 = Pawn("white", (1, 3))
white_pawn4 = Pawn("white", (1, 4))
white_pawn5 = Pawn("white", (1, 5))
white_pawn6 = Pawn("white", (1, 6))
white_pawn7 = Pawn("white", (1, 7))

black_rook1 = Rook("black", (7, 0))
black_knight1 = Knight("black", (7, 1))
black_bishop1 = Bishop("black", (7, 2))
black_queen = Queen("black", (7, 3))
black_king = King("black", (7, 4))
black_bishop2 = Bishop("black", (7, 5))
black_knight2 = Knight("black", (7, 6))
black_rook2 = Rook("black", (7, 7))

black_pawn0 = Pawn("black", (6, 0))
black_pawn1 = Pawn("black", (6, 1))
black_pawn2 = Pawn("black", (6, 2))
black_pawn3 = Pawn("black", (6, 3))
black_pawn4 = Pawn("black", (6, 4))
black_pawn5 = Pawn("black", (6, 5))
black_pawn6 = Pawn("black", (6, 6))
black_pawn7 = Pawn("black", (6, 7))






