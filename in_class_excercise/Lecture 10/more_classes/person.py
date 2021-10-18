'''
Sample Code
CS 5001, Fall 2020 - Lecture 10

A date class.
'''

class Person:
    '''
        Class -- Person
            Represents person.
        Attributes:
            firstname -- the Person's first name.
            lastname -- the Person's last name.
            dob -- the Person's date of birth, a Date object.
    '''
    def __init__(self, firstname, lastname, dob = None):
        '''
            Constructor -- creates a new instance of Person
            Parameters:
                self -- the current Person object
                firstname -- the Person's first name.
                lastname -- the Person's last name.
                dob -- the Person's date of birth, a Date object.
        '''
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
