'''
Fall2020
CS 5001 HW5
Yici Zhu
unittest for password.py
'''

from password import secure_password, lowercase, uppercase,\
                     digit, special_character, special_ch


def test_secure_password():
    assert(secure_password("#1234qazQ"))  # meet all requirements
    assert(secure_password("#qwawdqazQ"))  # no digit
    assert(secure_password("1qaz2wsx3edQ"))  # no sepcial char
    assert(not secure_password("#1234qazQQQQQQ"))  # exceeds limits
    assert(not secure_password("^1qaz2wsx3"))  # has other special char
    assert(not secure_password("qazwsxed#"))  # no upper & digits
    assert(not secure_password("#qwaw dqazQ"))  # has space


def test_lowercase():
    assert(not lowercase("1QAZ2WSX$$"))
    assert(lowercase("1qaz2$$"))
    assert(lowercase("1QWSEDCR2$$q"))


def test_uppercase():
    assert(uppercase("1QAZ2WS"))
    assert(not uppercase("1qqzwssx#!"))


def test_digit():
    assert(not digit("qazwsxedcQAZWSXX"))
    assert(digit("12qaz"))
    assert(digit("12QAZ#"))


def test_special_character():
    assert(special_character("!qazwsxedcQAZWSXX"))
    assert(not special_character("qazwsxedcQAZWSXX"))


def test_special_ch():
    assert(special_ch("!qazwsxedcQAZWSXX"))
    assert(not special_ch("%qazwsxedcQAZWSXX"))
    assert(not special_ch("!qazwsxed cQAZWSXX"))
