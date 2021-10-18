class OfficeHours:
    def __init__(self, day, start_hour, end_hour, location, host):
        self.day = day
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.location = location
        self.host = host

    def is_happing_at(self, time, day):
        return day == self.day and time >= self.start_hour \
            and time <= self.end_hour


def main():
    '''
    office_hours = {
        "day": "Tu",
        "start": 16,
        "end": 18,
        "location": "225, Huddle 1",
        "host": "Mr. T"
    }
    '''
    oh = OfficeHours("Tu", 16, 18, "225, Huddle 1", "Mr. T")
    print("Office hours are on", oh.day, "at", oh.start_hour)
    user_day = input("What day would you like to attend office hours? ")
    user_time = int(input("What time would you like to attend? (24-hour clock) "))
    while not oh.is_happening_at(user_time, user_day):
        print("No office hours at that time!")
        user_day = input("Enter a day:\n")
        user_time = int(input("Enter an hour:"))
    print("Office hours available!")


if __name__ == "__main__":
    main()