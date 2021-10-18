'''
Fall2020
CS 5001 HW5
Yici Zhu
it's a program validating password
'''


def secure_password(password):
    '''
    function-- secure_password
    it's a function to check if the input string
    meets all requirements of a password or not.
    parameter: password, string to check
    return:
    if meets all requirements, return True; if
    failed any of the requirement, retuern False
    '''
    maximum = 12
    minimum = 9
    requirements = 3
    if len(password) < minimum or len(password) > maximum:
        return False
    if lowercase(password) + uppercase(password) + digit(password)\
       + special_character(password) < requirements:
        return False
    if not special_ch(password):
        return False
    return True


def lowercase(password):
    '''
    function-- lowercase
    it's a function to check if the input string
    contains a lowercase letter
    parameter: password, string to check
    return:
    if the string contains at least one lowercase letter,
    return True, otherwise, False.
    '''
    for c in password:
        if c.islower():
            return True
    return False


def uppercase(password):
    '''
    function-- uppercase
    it's a function to check if the input string
    contains a uppercase letter
    parameter: password, string to check
    return:
    if the string contains at least one uppercase letter,
    return True, otherwise, False.
    '''
    for c in password:
        if c.isupper():
            return True
    return False


def digit(password):
    '''
    function-- digit
    it's a function to check if the input string
    contains a digit.
    parameter: password, string to check
    return:
    if the string contains at least one digit,
    return True, otherwise, False.
    '''
    for c in password:
        if c.isdigit():
            return True
    return False


def special_character(password):
    '''
    function-- special_character
    it's a function to check if the input string
    contains a required special character
    parameter: password, string to check
    return:
    if the string contains at least one special
    character, return True, otherwise, False.
    '''
    special_ch = "$#@!"
    for c in password:
        if c in special_ch:
            return True
    return False


def special_ch(password):
    '''
    function-- special_ch
    it's a function to check if the input string
    doesn't contains a special character other than
    the list given.
    parameter: password, string to check
    return:
    if the string contains other speicial character,
    return False. otherwise, True
    '''
    special_ch = "$#@!"
    for c in password:
        if not c.isnumeric() and not c.isalpha() and c not in special_ch:
            return False
    return True
