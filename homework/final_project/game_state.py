'''
Fall2020
CS 5001
Yici Zhu
Final Project
'''


import turtle
import time
from random import sample
from draw_utilities import draw_square_not_filled
from draw_utilities import draw_circle
from draw_utilities import draw_triangle
from piece import Piece
from move import Move


EMPTY = 0
BLACK = 1
RED = 2

NUM_SQUARES = 8  # The number of squares on each row.
SQUARE = 50  # The size of each square in the checkerboard.
KING_TRIAGLE_LENGTH = 35.35 # size of the triagle that marks king checker
KING_COLOR = "green"
KING_START_ANGLE = 120
AI_THINK_TIME = 0.5
HIGHLIGHT_COLOR = "red"
ORIGINAL_COLOR = "black"
BOARD_COLOR = "light gray"
CIRCLE_COLORS = ("black", "red")
CIRCLE = SQUARE / 2  # The size of each chess in the checkerboard
PLAYER_ROWS = 3
CORNER = (- NUM_SQUARES * SQUARE) / 2


class GameState:
    '''
    This is a class called GameState, contains fundamental rules of the game
    '''
    def __init__(self):
        '''
        The constructor for Gamestate class
        Attributes:
        square: store piece location in a nested list
        current_player: whose turn (red or black)
        selected_piece_index: index of selectd checker
        possible_moves = a list stores all possible moves
        '''
        self.square = [
            [EMPTY, Piece(BLACK), EMPTY, Piece(BLACK), EMPTY, Piece(BLACK), EMPTY, Piece(BLACK)],
            [Piece(BLACK), EMPTY, Piece(BLACK), EMPTY, Piece(BLACK), EMPTY, Piece(BLACK), EMPTY],
            [EMPTY, Piece(BLACK), EMPTY, Piece(BLACK), EMPTY, Piece(BLACK), EMPTY, Piece(BLACK)],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [Piece(RED), EMPTY, Piece(RED), EMPTY, Piece(RED), EMPTY, Piece(RED), EMPTY],
            [EMPTY, Piece(RED), EMPTY, Piece(RED), EMPTY, Piece(RED), EMPTY, Piece(RED)],
            [Piece(RED), EMPTY, Piece(RED), EMPTY, Piece(RED), EMPTY, Piece(RED), EMPTY],
        ]
        self.current_player = BLACK
        self.selected_piece_index = None # (xi, yi) of selected checker
        self.possible_moves = []


    def game_start(self):
        '''
        start the game, find all possible moves for current player
        '''
        self.find_all_possible_moves()


    def click_handler(self, x, y):
        '''
        Function -- click_handler
            Draw a line of a given length.
        Parameters:
            x: x-axis value in canvas
            y: y-axis value in canvas
        Returns:
            None
        '''
        (xi, yi) = self.axis_to_index(x, y)
        if self.check_if_out_of_board(xi, yi):
            # click outside of board, do nothing
            return
        current_click = self.square[xi][yi]

        if self.selected_piece_index is None:
            if current_click != EMPTY and current_click.color == self.current_player:
                # change to clicked state
                self.selected_piece_index  = (xi, yi)
                # draw highlight
                self.draw_highlight(xi, yi, False)

        else:
            clicked_on_a_possible_move = False
            peice = self.square[self.selected_piece_index[0]][self.selected_piece_index[1]]
            has_capture_move = any([move.is_capturing_move for move in peice.possible_moves])
            for move in peice.possible_moves:
                if xi == move.end[0] and yi == move.end[1] and \
                (not has_capture_move or (has_capture_move and move.is_capturing_move)):
                    # when clicked on a possible move, we need to look if there's possible capture
                    # move exist for this piece, if so, only allow capture move
                    clicked_on_a_possible_move = True
                    break
            if clicked_on_a_possible_move:
                # move checker -> (xi, yi)
                self.mark_king_if_necessary(xi, peice)
                self.move_checker(move)
                # switch player
                if self.current_player == BLACK:
                    self.current_player = RED
                else:
                    self.current_player = BLACK
                # re-calculate possible moves
                self.clear_all_possible_moves()
                self.find_all_possible_moves()
            # draw de-highlight
            self.draw_highlight(self.selected_piece_index[0], self.selected_piece_index[1], True)
            self.selected_piece_index = None

            # detect game end
            if len(self.possible_moves) == 0:
                self.game_end()
                return

            # make AI move when it's RED's turn
            if self.current_player == RED:
                self.ai_move()


    def game_end(self):
        '''
        Function -- game_end
            function decides who wins the game
            helper function for click-handler
        Parameters:
            None
        Returns:
            Nothing
        '''
        if self.current_player == BLACK:
            winning_player = "RED"
        else:
            winning_player = "BLACK"
        # remove click handler, game is ended
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.color("purple")
        pen.write(winning_player + " PLAYER WINS!", align="center", font=("Arial", 25, "normal"))
        screen = turtle.Screen()
        screen.onclick(None)


    def ai_move(self):
        '''
        Function -- ai_move
            function for how AI player move
        Parameters:
            None
        Returns:
            nothing return. helper function for click_handler.
        '''
        turtle.update()
        # fake AI think for 0.5s (for better visibility)
        time.sleep(AI_THINK_TIME)
        move = self.possible_moves[0]
        # (make AI a little better - if move is not a capture move, then use random index instead of first one)
        if move.is_capturing_move is False:
            move = sample(self.possible_moves, 1)[0]
        peice = self.square[move.start[0]][move.start[1]]
        self.mark_king_if_necessary(move.end[0], peice)
        self.move_checker(move)
        # switch back to human player
        self.current_player = BLACK
        # re-calculate possible moves
        self.clear_all_possible_moves()
        self.find_all_possible_moves()
        # detect game end
        if len(self.possible_moves) == 0:
            self.game_end()
            return


    def mark_king_if_necessary(self, xi, piece):
        '''
        Function -- mark_king_if_necessary
            when chess reached the "king row", it
            will be marked as a king chess
        Parameters:
            xi: index of x
            piece: the piece to be checked
        Returns:
            Nothing
        '''
        if piece.color == BLACK:
            target_king_row = len(self.square) - 1
        else:
            target_king_row = 0
        if xi == target_king_row:
            piece.mark_as_king()


    def check_if_out_of_board(self, row, col):
        '''
        Function -- check_if_out_of_board
            check if clicked out of the board
        Parameters:
            row: represent row
            col: represent column
        Returns:
            return True if clicked outside the board
            False if clicked in board
        '''
        if row < 0 or row >= len(self.square) or col < 0 or col >= len(self.square[0]):
            # click outside of board
            return True
        return False


    def clear_all_possible_moves(self):
        '''
        Function -- clear_all_possible_moves
            clear possible moves in order to recalculate
        Parameters:
            None
        Returns:
            Nothing
        '''
        self.possible_moves = []
        for row in range(len(self.square)):
            for col in range(len(self.square[0])):
                if self.square[row][col] == EMPTY:
                    continue
                piece = self.square[row][col]
                piece.possible_moves = []


    def find_all_possible_moves(self):
        '''
        Function -- find_all_possible_moves
            store all possible moves in a list
        Parameters:
            None
        Returns:
            Nothing
        '''
        for row in range(len(self.square)):
            for col in range(len(self.square[0])):
                if self.square[row][col] == EMPTY:
                    continue
                piece = self.square[row][col]
                if piece.color == self.current_player:
                    for direction in piece.directions:
                        move_row = row + direction[0]
                        move_col = col + direction[1]
                        if self.check_if_out_of_board(move_row, move_col):
                            continue
                        elif self.square[move_row][move_col] == EMPTY:
                            # create a non-capture move
                            move = Move([row, col], [move_row, move_col], False)
                            self.possible_moves.append(move)
                            piece.add_possible_move(move)
                        elif self.square[move_row][move_col].color != self.current_player:
                            move_row_cap = move_row + direction[0]
                            move_col_cap = move_col + direction[1]
                            if self.check_if_out_of_board(move_row_cap, move_col_cap):
                                continue
                            elif self.square[move_row_cap][move_col_cap] == EMPTY:
                                all_captured_and_destination_list = [([move_row, move_col], [move_row_cap, move_col_cap])] # contains a list of tuple (captured piece indices, end indices)
                                self.find_capture_move([move_row_cap, move_col_cap], piece.directions, all_captured_and_destination_list)
                                # now we have all possible captured position, add them to possible_moves one by one
                                captured_list = []
                                for (capture_indices, dest_indices) in all_captured_and_destination_list:
                                    captured_list.append(capture_indices)
                                    move = Move([row, col], dest_indices, True)
                                    move.captured_piece.extend(captured_list)
                                    self.possible_moves.insert(0, move)
                                    piece.add_possible_move(move)


    def find_capture_move(self, start, dirs, result):
        '''
        Function -- find_capture_move
            store all possible moves in a list
        Parameters:
            start:start point
            dirs: directions to search
            result: a list to save found possible moves as [(captured piece, end point)]
        '''
        for dir in dirs:
            move_row = start[0] + dir[0]
            move_col = start[1] + dir[1]
            if self.check_if_out_of_board(move_row, move_col) or self.square[move_row][move_col] == EMPTY:
                continue
            elif self.square[move_row][move_col].color != self.current_player:
                # find opponent piece, check if empty in same dir
                move_row_dir = move_row + dir[0]
                move_col_dir = move_col + dir[1]
                if self.check_if_out_of_board(move_row_dir, move_col_dir):
                    continue
                elif self.square[move_row_dir][move_col_dir] == EMPTY:
                    # find another possible multiple capture move, check if captured piece has already been found
                    # if not continue calling this function to explore more move
                    if self.check_if_captured_piece_already_exist(move_row, move_col, result) is False:
                        result.append(([move_row, move_col], [move_row_dir, move_col_dir]))
                        self.find_capture_move([move_row_dir, move_col_dir], dirs, result)


    def check_if_captured_piece_already_exist(self, xi, yi, capture_list):
        for (capture_piece_indices, _) in capture_list:
            if xi == capture_piece_indices[0] and yi == capture_piece_indices[1]:
                return True
        return False


    def axis_to_index(self, x, y):
        '''
        Function -- axis_to_index
            convert axis to index
        Parameters:
            x: x-axis value in canvas
            y: y-axis value in canvas
        Returns:
            index of x and index of y
        '''
        x = x + (SQUARE * NUM_SQUARES) / 2
        y = y + (SQUARE * NUM_SQUARES) / 2
        xi = x // SQUARE
        yi = y // SQUARE
        return (int(yi), int(xi)) # axis and index are reverted


    def index_to_axis(self, yi, xi):
        '''
        Function -- index_to_axis
            convert index to axis
        Parameters:
            xi: index of x
            yi: index of y
        Returns:
            return axis X & y
        '''
        x = xi * SQUARE
        y = yi * SQUARE
        x = x - (SQUARE * NUM_SQUARES) / 2
        y = y - (SQUARE * NUM_SQUARES) / 2
        return (x, y)


    def draw_highlight(self, xi, yi, is_remove):
        (x, y) = self.index_to_axis(xi, yi)
        pen = turtle.Turtle()  # This variable does the drawing.
        pen.penup()  # This allows the pen to be moved.
        pen.hideturtle()  # This gets rid of the triangle cursor.
        if is_remove is True:
            pen.color(ORIGINAL_COLOR)
        else:
            pen.color(HIGHLIGHT_COLOR)
        pen.setposition(x, y)
        draw_square_not_filled(pen, SQUARE)


    def draw_checker(self, xi, yi, is_remove, is_king):
        (x, y) = self.index_to_axis(xi, yi)
        x += SQUARE/2 # we need to draw circle, move x half SQUARE to the right
        pen = turtle.Turtle()  # This variable does the drawing.
        pen.penup()  # This allows the pen to be moved.
        pen.hideturtle()  # This gets rid of the triangle cursor.
        if is_remove is True:
            pen.color(BOARD_COLOR, BOARD_COLOR)
        else:
            if self.current_player == BLACK:
                pen.color(CIRCLE_COLORS[0], CIRCLE_COLORS[0])
            else:
                pen.color(CIRCLE_COLORS[1], CIRCLE_COLORS[1])
        pen.setposition(x, y)
        draw_circle(pen, CIRCLE)
        # draw a triagle if this is a king
        if is_king is True and is_remove is False:
            pen.right(KING_START_ANGLE)
            pen.color(KING_COLOR, KING_COLOR)
            pen.setposition(x, y + SQUARE)
            draw_triangle(pen, KING_TRIAGLE_LENGTH)


    def move_checker(self, move):
        previous_index = move.start
        new_index = move.end
        piece = self.square[previous_index[0]][previous_index[1]]
        #1 update square table
        self.square[previous_index[0]][previous_index[1]] = EMPTY
        self.square[new_index[0]][new_index[1]] = piece
        if move.is_capturing_move:
            # clear each one of captured piece to EMPTY
            for capture in move.captured_piece:
                self.square[capture[0]][capture[1]] = EMPTY

        #2 remove checker from previous position
        self.draw_checker(previous_index[0], previous_index[1], True, piece.is_king)
        if move.is_capturing_move:
            # remove all captured pieces
            for capture in move.captured_piece:
                self.draw_checker(capture[0], capture[1], True, piece.is_king)

        #3 draw new checker in new position
        self.draw_checker(new_index[0], new_index[1], False, piece.is_king)
