'''
Fall2020
CS 5001 HW3
Yici Zhu
it's the unitest for sizefinder.py
'''

from sizefinder import check_input_valid
from sizefinder import get_shirt_size
from sizefinder import get_shirt_size_by_step


def test_check_input_valid():
    assert(check_input_valid(22) is False)
    assert(check_input_valid(53) is False)
    assert(check_input_valid(28) is True)


def test_get_shirt_size():
    assert(get_shirt_size(22, 'k') == "not available")
    assert(get_shirt_size(36, 'w') == "XL")
    assert(get_shirt_size(48, 'm') == "XXL")
    assert(get_shirt_size(22, 'unknown') == 0)


def test_get_shirt_size_by_step():
    assert(get_shirt_size_by_step(12, 15, 30, 2) == "not available")
    assert(get_shirt_size_by_step(35, 15, 30, 2) == "not available")
    assert(get_shirt_size_by_step(26, 26, 36, 2) == "S")
    assert(get_shirt_size_by_step(28.5, 26, 36, 2) == "M")
    assert(get_shirt_size_by_step(31.9, 26, 36, 2) == "L")
    assert(get_shirt_size_by_step(32, 26, 36, 2) == "XL")
    assert(get_shirt_size_by_step(35, 26, 36, 2) == "XXL")
    assert(get_shirt_size_by_step(41, 30, 42, 2) == "XXXL")
