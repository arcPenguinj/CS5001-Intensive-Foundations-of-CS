'''
Fall2020
CS 5001
Yici Zhu
Final Project
'''

class Move:
    def __init__(self, start, end, is_capturing_move):
        self.start = start
        self.end = end
        self.is_capturing_move = is_capturing_move
        self.captured_piece = []
