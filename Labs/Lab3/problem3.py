def greeting(name):
    greeting = "Hello " + name
    return greeting

def current_days(days):
    if days == "F":
        return 0
    elif days == "Sa":
        return -2
    elif days == "Su":
        return -1
    elif days == "M":
        return 1
    elif days == "Tu":
        return 2
    elif days == "W":
        return 3
    elif days == "Th":
        return 4

def days_until_friday(current_days):
    days_until_friday = 5 - current_days
    return days_until_friday

def main():
    name = input("What your name: ")
    days = input("What's the current day: ")
    greetings = greeting(name)
    print(greetings)
    daysnumber = current_days(days)
    answer = days_until_friday(daysnumber)
    print(answer)


if __name__ == "__main__":
    main()