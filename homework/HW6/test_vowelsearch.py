from vowelsearch import r_contain_vowel
from vowelsearch import contains_vowel


def test_r_contain_vowel():
    assert (r_contain_vowel(" ") is False)
    assert (r_contain_vowel("") is False)
    assert (r_contain_vowel("😍😊😂😂❤") is False)
    assert (r_contain_vowel("12345") is False)
    assert (r_contain_vowel("#abc") is True)
    assert (r_contain_vowel("354abc") is True)
    assert (r_contain_vowel("hello") is True)


def test_contains_vowel():
    assert (contains_vowel([]) is False)
    assert (contains_vowel([" ", " "]) is False)
    assert (contains_vowel(["garage", "this", "man"]) is True)
    assert (contains_vowel(["fff", "this", "man"]) is False)
    assert (contains_vowel(["❤abc", "#abc", "123abc"]) is True)
    assert (contains_vowel(["", "#bc", "123abc"]) is False)
