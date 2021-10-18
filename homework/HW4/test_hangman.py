'''
Fall2020
CS 5001 HW3
Yici Zhu
unit test for hangman
'''

from hangman import generate_word


def test_generate_word():
    assert (generate_word("APPLE", "A") == "A____")
    assert (generate_word("APPLE", "APPLE") == "APPLE")
    assert (generate_word("OBVIOUS", "A") == "_______")
    assert (generate_word("OBVIOUS", "AO") == "O___O__")
    assert (generate_word("XYLOPHONE", "OE") == "___O__O_E")


# There is an input in run_game function, can move the whole
# function into main function; but both way will not have unittest.
# Prefer to have a seperate function to run every single round of the game
