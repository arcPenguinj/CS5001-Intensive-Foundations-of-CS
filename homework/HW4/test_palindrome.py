'''
Fall2020
CS 5001 HW3
Yici Zhu
unit test for palindrome
'''

from palindrome import is_palindrome


def test_is_palindrome():
    assert (is_palindrome("RADar") is True)
    assert (is_palindrome("!radar!") is True)
    assert (is_palindrome("madam Im adam") is True)
    assert (is_palindrome("a") is False)
    assert (is_palindrome("abcd") is False)
