'''
Fall2020
CS 5001
Yici Zhu
Final Project
'''


BLACK = 1
RED = 2
UPPER_LEFT = [1, -1]
UPPER_RIGHT= [1, 1]
LOWER_LEFT = [-1, -1]
LOWER_RIGHT = [-1, 1]


class Piece:
    def __init__(self, color):
        self.color = color
        self.directions = self.init_directions()
        self.is_king = False
        self.possible_moves = []


    def init_directions(self):
        if self.color == BLACK:
            return [UPPER_LEFT, UPPER_RIGHT]
        else:
            return [LOWER_LEFT, LOWER_RIGHT]


    def add_possible_move(self, move):
        self.possible_moves.append(move)


    def reset_possible_move(self):
        self.possible_moves = []


    def mark_as_king(self):
        self.is_king = True
        self.directions = [UPPER_LEFT, UPPER_RIGHT, LOWER_LEFT, LOWER_RIGHT]
