'''
Sample Code
CS 5001, Fall 2020 - Lecture 9

A playing card class.
'''

class PlayingCard:
    '''
        Class -- PlayingCard
            Represents a playing card.
        Attributes:
            value -- the card's value, an integer.
            suit -- the card's suit, a string
    '''
    name = None

    def __init__(self, value, suit):
        '''
            Constructor -- creates a new instance of PlayingCard
            Parameters:
                self -- the current PlayingCard object
                value -- the card's value, an integer
                suit -- the card's suit, a string
        '''
        self.value = value
        self.suit = suit
        self.set_name()
    
    def set_name(self):
        '''
            Method -- set_name
                Helper method to set the name of special cards.
            Parameter:
                self -- The current PlayingCard object
            Returns:
                Nothing. Sets the name attribute if applicable.
        '''
        NAMES = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }
        if self.value in NAMES:
            self.name = NAMES[self.value]

    def __str__(self):
        '''
            Method -- __str__
                Creates a string representation of the PlayingCard
            Parameter:
                self -- The current PlayingCard object
            Returns:
                A string representation of the PlayingCard.
        '''
        if self.name is not None:
            return "{} of {}".format(self.name, self.suit)
        return "{} of {}".format(self.value, self.suit)
    
    def __eq__(self, other):
        '''
            Method -- __eq__
                Checks if two objects are equal
            Parameters:
                self -- The current PlayingCard object
                other -- An object to compare self to.
            Returns:
                True if the two objects are equal, False otherwise.
        '''
        if type(self) != type(other):
            return False
        return self.value == other.value and self.suit == other.suit


def main():
    ten_diamonds = PlayingCard(10, "Diamonds")
    ace_hearts = PlayingCard(1, "Hearts")
    print(ten_diamonds)
    print(ace_hearts)


if __name__ == "__main__":
    main()