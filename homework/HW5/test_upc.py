'''
Fall2020
CS 5001 HW5
Yici Zhu
unittest for upc.py
'''

from upc import is_valid_upc


def test_is_valid_upc():
    assert(is_valid_upc("t12345") is False)
    assert(is_valid_upc("9781484234310") is True)
    assert(is_valid_upc("#6876546") is False)
    assert(is_valid_upc("978031415410") is False)
    assert(is_valid_upc(" 6876546") is False)
    assert(is_valid_upc("9781484 2343101") is False)
