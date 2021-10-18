'''
Sample Code
CS 5001, Fall 2020 - Lecture 10

A date class.
'''

class Date:
    '''
        Class -- Date
            Represents a calendar date.
        Attributes:
            month -- the month, an integer from 1 to 12.
            day -- the day of the month, an integer from 1 to 31
            year -- the year, a 4-digit integer
    '''
    def __init__(self, month, day, year):
        '''
            Constructor -- creates a new instance of Date
            Parameters:
                self -- the current Date object
                month -- the month, an integer from 1 to 12.
                day -- the day of the month, an integer from 1 to 31
                year -- the year, a 4-digit integer
        '''
        self.month = month
        self.day = day
        self.year = year
