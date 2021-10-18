'''
Fall2020
CS 5001 HW5
Yici Zhu
it's a program to check vowels
'''

VOEWL = "aeiou"


def r_contain_vowel(s):
    '''
    function-- r_contain_vowel
    it's a function to check if there is a vowel in the string
    parameter:
    s - string
    return:
    if string is empty, return false; if it's not, check the letter
    in string one by one, once meet a VOWEL, return true.
    '''
    s = s.lower()
    if len(s) == 0:
        return False
    if len(s) >= 1:
        if s[0] in VOEWL:
            return True
        else:
            return r_contain_vowel(s[1:])


def contains_vowel(lst):
    '''
    function-- contains_vowel
    it's a function to check if each string in the list has at least
    one vowel
    parameter:
    lst - a list of strings
    return:
    if list is empty, return false; if it's not, call last function to
    check if each string in the list has vowel, if all the strings in the
    list contain vowel, return true
    '''
    if len(lst) == 0:
        return False
    if len(lst) == 1:
        return r_contain_vowel(lst[0])
    if len(lst) > 1:
        return r_contain_vowel(lst[0]) and contains_vowel(lst[1:])
