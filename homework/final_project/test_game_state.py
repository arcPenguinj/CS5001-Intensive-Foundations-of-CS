'''
Fall2020
CS 5001
Yici Zhu
Final Project
'''

from game_state import GameState
from game_state import NUM_SQUARES
from game_state import BLACK
from game_state import RED
from piece import Piece

def test_constructor():
    game_state = GameState()
    assert(len(game_state.possible_moves) == 0)
    assert(game_state.selected_piece_index == None)
    assert(len(game_state.square) == NUM_SQUARES)
    assert(len(game_state.square[0]) == NUM_SQUARES)
    assert(game_state.current_player == BLACK)


def test_game_start():
    game_state = GameState()
    game_state.game_start()
    assert(len(game_state.possible_moves) > 0)


def test_click_handler():
    game_state = GameState()
    game_state.game_start()

    # initially no selected piece
    # assert(game_state.selected_piece_index == None)

    # # clicked on empty space, do nothing
    # game_state.click_handler(0, 0)
    # assert(game_state.selected_piece_index == None)

    # # clicked on Black piece, save it to selected_piece_index
    # game_state.click_handler(-131, -74)
    # assert(game_state.selected_piece_index == (2,1))

    # # now click outside of board, do nothing
    # game_state.click_handler(-218, 68)
    # assert(game_state.selected_piece_index == (2,1))

    # # click on invalid move, selection should be removed
    # game_state.click_handler(-178, -122)
    # assert(game_state.selected_piece_index == None)


def test_mark_king_if_necessary():
    game_state = GameState()
    piece_black = Piece(BLACK)
    piece_red = Piece(RED)

    # test black piece, xi should be NUM_SQUARES - 1 to become a king
    game_state.mark_king_if_necessary(0, piece_black)
    assert(piece_black.is_king is False)
    game_state.mark_king_if_necessary(NUM_SQUARES - 1, piece_black)
    assert(piece_black.is_king is True)

    # test red piece, xi should be 0 to become a king
    game_state.mark_king_if_necessary(NUM_SQUARES - 1, piece_red)
    assert(piece_red.is_king is False)
    game_state.mark_king_if_necessary(0, piece_red)
    assert(piece_red.is_king is True)


def test_check_if_out_of_board():
    game_state = GameState()
    assert(game_state.check_if_out_of_board(-1, 4) is True)
    assert(game_state.check_if_out_of_board(1, -4) is True)
    assert(game_state.check_if_out_of_board(1, 4) is False)
    assert(game_state.check_if_out_of_board(NUM_SQUARES, 4) is True)
    assert(game_state.check_if_out_of_board(1, NUM_SQUARES) is True)
    assert(game_state.check_if_out_of_board(NUM_SQUARES-1, NUM_SQUARES-4) is False)


def test_clear_all_possible_moves():
    game_state = GameState()
    game_state.game_start()
    assert(len(game_state.possible_moves) > 0)
    assert(len(game_state.square[2][1].possible_moves) > 0)
    game_state.clear_all_possible_moves()
    assert(len(game_state.possible_moves) == 0)
    assert(len(game_state.square[2][1].possible_moves) == 0)


def test_find_all_possible_moves():
    game_state = GameState()
    game_state.find_all_possible_moves()
    assert(len(game_state.possible_moves) > 0)
    assert(len(game_state.square[2][1].possible_moves) > 0)


def test_check_if_captured_piece_already_exist():
    game_state = GameState()
    capture_list = [([1,2], []), ([3,4], [])]
    assert(game_state.check_if_captured_piece_already_exist(1, 2, capture_list) is True)
    assert(game_state.check_if_captured_piece_already_exist(3, 2, capture_list) is False)


def test_axis_to_index():
    game_state = GameState()
    assert(game_state.axis_to_index(0, 0) == (4, 4))
    assert(game_state.axis_to_index(-50, 50) == (5, 3))
    assert(game_state.axis_to_index(-100, -100) == (2, 2))
    assert(game_state.axis_to_index(100, 100) == (6, 6))


def test_index_to_axis():
    game_state = GameState()
    assert(game_state.index_to_axis(0, 0) == (-200, -200))
    assert(game_state.index_to_axis(2, 6) == (100, -100))
    assert(game_state.index_to_axis(6, 7) == (150, 100))
    assert(game_state.index_to_axis(6, 2) == (-100, 100))
