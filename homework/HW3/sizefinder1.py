'''
Fall2020
CS 5001 HW3
Yici Zhu
it's a program for helping find a size
'''


def mens_size(chest_size):
    '''
    Function -- mens_size
    to cpompare input by using chest size chart below
    Parameters:
    chest_size -- expecting a size >=34 and <53
    Returns:
    if input is valid, then return a size,
    if not valid, then return "not available"
    '''
    if chest_size >= 34 and chest_size < 37:
        return "S"
    elif chest_size >= 37 and chest_size < 40:
        return "M"
    elif chest_size >= 40 and chest_size < 43:
        return "L"
    elif chest_size >= 43 and chest_size < 47:
        return "XL"
    elif chest_size >= 47 and chest_size < 50:
        return "XXL"
    elif chest_size >= 50 and chest_size < 53:
        return "XXXL"
    else:
        return "not available"


def womens_size(chest_size):
    '''
    Function -- womens_size
    to cpompare input by using chest size chart below
    Parameters:
    chest_size -- expecting a size >=30 and <42
    Returns:
    if input is valid, then return a size,
    if not valid, then return "not available"
    '''
    if chest_size >= 30 and chest_size < 32:
        return "S"
    elif chest_size >= 32 and chest_size < 34:
        return "M"
    elif chest_size >= 34 and chest_size < 36:
        return "L"
    elif chest_size >= 36 and chest_size < 38:
        return "XL"
    elif chest_size >= 38 and chest_size < 40:
        return "XXL"
    elif chest_size >= 40 and chest_size < 42:
        return "XXXL"
    else:
        return "not available"


def kids_size(chest_size_in):
    '''
    Function -- womens_size
    to cpompare input by using chest size chart below
    Parameters:
    chest_size -- expecting a size >=26 and <36
    Returns:
    if input is valid, then return a size,
    if not valid, then return "not available"
    '''
    if chest_size_in >= 26 and chest_size_in < 28:
        return "S"
    elif chest_size_in >= 28 and chest_size_in < 30:
        return "M"
    elif chest_size_in >= 30 and chest_size_in < 32:
        return "L"
    elif chest_size_in >= 32 and chest_size_in < 34:
        return "XL"
    elif chest_size_in >= 34 and chest_size_in < 36:
        return "XXL"
    else:
        return "not available"


def main():

    chest_size = float(input("Chest measurement in inches: "))

    k = kids_size(chest_size)
    w = womens_size(chest_size)
    m = mens_size(chest_size)

    if k == "not available" and w == "not available" and m == "not available":
        print("Sorry, we don't carry your size")
    else:
        print("Your size choices:")
        print("Kids size: " + k)
        print("Womens size: " + w)
        print("Mens size: " + m)


if __name__ == "__main__":
    main()
