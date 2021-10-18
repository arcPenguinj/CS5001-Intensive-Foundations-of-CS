'''
Yici Zhu
CS 5001, Fall 2020
it's a program calculating racepace
test cases :
5km, 0 hours, 30 minutes => 3.11 miles, 9:40 pace, 6.21 MPH
10km, 3 hours, 0 minutes => 6.21 miles, 28:59 pace, 2.07 MPH
15km, 5 hours, 30 minutes => 9.32 miles, 35:25 pace, 1.69 MPH
'''

def main ():
    kilo_run = float (input ('How many kilometers did you run? '))
    hours_number = int (input ('What was your finish time? Enter hours: '))
    minutes_number = int (input ('Enter minutes: '))

    mile_run = kilo_run / 1.61
    pace = (hours_number * 60 + minutes_number) / mile_run
    paceseconds = (pace - int (pace)) * 60
    paceminute = int (pace)
    mph = mile_run / (hours_number + (minutes_number/60))

    print (str(round (mile_run,2)) + " miles, " + str(paceminute) + ":" + str(round(paceseconds)) + " pace, " + str(round(mph,2)) + " MPH")


if __name__ == "__main__":
    main()