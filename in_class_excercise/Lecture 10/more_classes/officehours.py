'''
Sample Code
CS 5001, Fall 2020 - Lecture 9

Representing office hours using a class.
'''


class OfficeHours:
    '''
        Class -- OfficeHours
            Represents an office hours session.
        Attributes:
            start_hour -- The hour that the session starts (24-hour clock).
            end_hour -- The hour that the session ends (24-hour clock).
            day -- The day of the week, a string.
            location -- The location of the office hours, a string.
            host -- The name of the person hosting office hours.
        Methods:
            is_happening_at -- Checks if the office hours are taking place at a
            given time on a given day.
    '''

    def __init__(self, start_hour, end_hour, day, location, host):
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.day = day
        self.location = location
        self.host = host

    def is_happening_at(self, time, day):
        '''
            Method -- is_happening_at
                Checks if this office hours session is happening at the given
                time on the given day.
            Parameters:
                self -- The current OfficeHours object.
                time -- The hour of the day (24 hour clock), an integer.
                day -- The day of the week.
            Returns:
                True if the office hours session will be happening at the specified
                time and day, False otherwise.
        '''
        return day == self.day and time >= self.start_hour and \
            time <= self.end_hour

def main():
    oh = OfficeHours(16, 18, "Tu", "225, Huddle 1", "Mr. T")
    user_day = input("What day would you like to attend office hours? ")
    user_time = int(input("What time would you like to attend? (24-hour clock) "))
    while not oh.is_happening_at(user_time, user_day):
        print("No office hours at that time!")
        user_day = input("Enter a day:\n")
        user_time = int(input("Enter an hour:"))
    print("Office hours available!")


if __name__ == "__main__":
    main()