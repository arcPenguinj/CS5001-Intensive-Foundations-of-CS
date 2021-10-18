'''
Fall2020
CS 5001 HW3
Yici Zhu
it's the unitest for sizefinder.py
'''

from sizefinder import mens_size
from sizefinder import womens_size
from sizefinder import kids_size


def test_mens_size():
    assert(mens_size(22) == "not available")
    assert(mens_size(34) == "S")
    assert(mens_size(38) == "M")
    assert(mens_size(41) == "L")
    assert(mens_size(43) == "XL")
    assert(mens_size(49) == "XXL")
    assert(mens_size(52) == "XXXL")
    assert(mens_size(53) == "not available")


def test_womens_size():
    assert(womens_size(29) == "not available")
    assert(womens_size(31.1) == "S")
    assert(womens_size(33.9) == "M")
    assert(womens_size(34.99) == "L")
    assert(womens_size(37) == "XL")
    assert(womens_size(39.9) == "XXL")
    assert(womens_size(40) == "XXXL")
    assert(womens_size(55.5) == "not available")


def test_kids_size():
    assert(kids_size(20) == "not available")
    assert(kids_size(26.55) == "S")
    assert(kids_size(28.55) == "M")
    assert(kids_size(30) == "L")
    assert(kids_size(33) == "XL")
    assert(kids_size(35) == "XXL")
    assert(kids_size(50.5) == "not available")
