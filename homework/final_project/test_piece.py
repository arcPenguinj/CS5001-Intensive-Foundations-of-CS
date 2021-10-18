'''
Fall2020
CS 5001
Yici Zhu
Final Project
'''

from piece import Piece
from piece import BLACK
from piece import RED


def test_constructor():
    piece = Piece(BLACK)
    assert(piece.color == BLACK)
    assert(len(piece.directions) == 2)
    assert(piece.is_king is False)
    assert(len(piece.possible_moves) == 0)
    piece = Piece(RED)
    assert(piece.color == RED)


def test_add_possible_moves():
    piece = Piece(BLACK)
    piece.add_possible_move('fake_move')
    assert(len(piece.possible_moves) == 1)
    piece.add_possible_move('fake_move')
    assert(len(piece.possible_moves) == 2)


def test_reset_possible_moves():
    piece = Piece(BLACK)
    assert(len(piece.possible_moves) == 0)
    piece.add_possible_move('fake_move')
    assert(len(piece.possible_moves) == 1)
    piece.reset_possible_move()
    assert(len(piece.possible_moves) == 0)


def test_mark_as_king():
    piece = Piece(BLACK)
    assert(piece.is_king is False)
    piece.mark_as_king()
    assert(piece.is_king is True)
