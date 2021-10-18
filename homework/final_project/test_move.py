'''
Fall2020
CS 5001
Yici Zhu
Final Project
'''


from move import Move


def test_constructor():
    move = Move([0,0], [2,2], True)
    assert(move.start == [0,0])
    assert(move.end == [2,2])
    assert(move.is_capturing_move is True)
    assert(move.captured_piece == [])
