'''
Fall2020
CS 5001 HW3
Yici Zhu
it's a program for travel expense
'''


def calculate_mileage(start, end):
    '''
    Function -- calculate_mileage
    Calculates miles driven using the start and end odometer values.
    Parameters:
    start -- The odometer reading at the start of the trip. Expecting a
    number greater than 0.
    end -- The odometer reading at the end of the trip. Expecting a
    number greater than 0 and greater than the start value.
    Returns:
    The miles driven, a number. If either parameter is invalid (e.g.
    either parameter is negative or end is less than start), returns 0.
    '''
    if start < 0 or end < start:
        return 0
    return end - start


def get_reimbursement_amount(mileage):
    '''
    Function -- get_reimbursement_amount
    Calculates the amount in dollars that the employee should be
    reimbursed based on their mileage and the standard rate per mile.
    The standard rate for 2020 is 57.5 cents per mile.
    Parameters:
    mileage -- The number of miles driven.
    Returns:
    The amount the employee should be reimbursed in dollars, a float
    rounded to 2 decimal places.
    '''
    standard_rate = 0.575
    return round(standard_rate * mileage, 2)


def get_actual_mileage_rate(mpg, fuel_price):
    '''
    Function -- get_actual_mileage_rate
    Calculates the actual trip cost per mile in dollars based on the
    car's MPG and the fuel price.
    Parameters:
    mpg -- The car's miles per gallon (MPG), an integer greater than 0.
    fuel_price -- The fuel cost in dollars per gallon, a non-negative
    float.
    Returns:
    The actual cost per mile in dollars, a float rounded to 4 decimal
    places. If supplied arguments are invalid, returns 0.0
    '''
    if mpg <= 0 or fuel_price < 0:
        return 0.0
    return round(fuel_price / mpg, 4)


def get_actual_trip_cost(start, end, mpg, fuel_price):
    '''
    Function -- get_actual_trip_cost
    Calculates the cost of a trip in dollars based on the miles driven,
    the MPG of the car, and the fuel price per gallon.
    Parameters:
    start -- The odometer reading at the start of the trip. Expecting a
    number greater than 0.
    end -- The odometer reading at the end of the trip. Expecting a
    number greater than 0 and greater than the start value.
    mpg -- The car's miles per gallon (MPG), an integer greater than 0.
    fuel_price -- The fuel price per gallon, a non-negative float.
    Returns:
    The cost of the drive in dollars, a float rounded to 2 decimal
    places. If any of the supplied arguments are invalid, returns 0.0
    '''
    mileage_driven = calculate_mileage(start, end)
    actual_rate = get_actual_mileage_rate(mpg, fuel_price)
    return round(mileage_driven * actual_rate, 2)


def main():
    print("MILEAGE REIMBURSEMENT CALCULATOR")
    print("Options:")
    print("1 - Calculate reimbursement amount from odometer readings")
    print("2 - Calculate reimbursement amount from miles traveled")
    print("3 - Calculate the actual cost of your trip")
    choice = input(("Enter your choice (1, 2, or 3): "))
    if choice == "1" or choice == "3":
        starting = float(input("Enter your starting odometer reading: "))
        ending = float(input("Enter your ending odometer reading: "))
        if choice == "1":
            reimburse_mile = float(calculate_mileage(starting, ending))
            reimburse_amount = float(get_reimbursement_amount(reimburse_mile))
        else:
            mpg = float(input("Enter your car's MPG: "))
            fuel_price = float(input("Enter the fuel price per gallon: "))
            trip_cost = get_actual_trip_cost(starting, ending, mpg, fuel_price)
    elif choice == "2":
        traveled = float(input("Enter the number of miles traveled: "))
        reimburse_amount = float(get_reimbursement_amount(traveled))
    else:
        print("Not a valid choice")

    if choice == "1" or choice == "2":
        print("You will be reimbursed $" + str(reimburse_amount))
    else:
        print("Your trip cost $" + str(trip_cost))


if __name__ == "__main__":
    main()
