'''
Fall2020
CS 5001 HW2
Yici Zhu
it's a program for planning exercise based on different conditions

'''


def main():
    days = input("What day is it? ").title()
    holidays = input("Is it a holiday? ").title()
    rains = input("Is it raining? ").title()
    temps = float(input("What is the temperature? "))

    # print(days, holidays, rains, temps)

    holidaybool = True
    workoutdays_bool = True
    rainsbool = True

    if days != "M" and days != "Tu" and days != "W" and days != "Th" and \
       days != "F" and days != "Sa" and days != "Su":
        print("Swim for 35 minutes")
        return

    if holidays == "Y":
        holidaybool = True
    elif holidays == "N":
        holidaybool = False
    else:
        print("Swim for 35 minutes")
        return

    if rains == "Y":
        rainsbool = True
    elif rains == "N":
        rainsbool = False
    else:
        print("Swim for 35 minutes")
        return

    if days == "M" or days == "W" or days == "F" or \
       days == "Sa" or holidaybool:
        workoutdays_bool = True
    else:
        print("Take a rest day")
        return

    excersice = ""

    if days == "M" or days == "W" or days == "F":
        excersice = "Run"
    if days == "Sa" or holidaybool:
        excersice = "Hike"
    if rainsbool and workoutdays_bool:
        excersice = "Swim"

    excersice_time = ""

    if excersice == "Run" and (temps > 75 or temps < 35):
        excersice_time = "30"
    else:
        excersice_time = "45"

    print(excersice + " for " + excersice_time + " minutes")


if __name__ == "__main__":
    main()
