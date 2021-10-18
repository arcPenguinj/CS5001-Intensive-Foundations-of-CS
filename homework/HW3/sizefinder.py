'''
Fall2020
CS 5001 HW3
Yici Zhu
it's a program for helping find a size
'''


def check_input_valid(chest_size):
    '''
    Function -- check_input_valid
    to check whether the value is True or Flase
    Parameters:
    chest_size -- expecting a size >=26 and <53,
    Returns:
    if input is valid, then return True
    if not valid, then return False
    '''
    if chest_size < 26 or chest_size >= 53:
        return False
    return True


def get_shirt_size(chest_size, type):
    '''
    Function -- get_shirt_size
    according to type, finding shirt size
    Parameters:
    chest_size --customer's input
    type -- kid/women/men
    Returns:
    call the function "get_shirt_size_by_step"
    by using different parameters to get size.
    '''
    if type == "k":
        return get_shirt_size_by_step(chest_size, 26, 36, 2)
    elif type == "w":
        return get_shirt_size_by_step(chest_size, 30, 42, 2)
    elif type == "m":
        return get_shirt_size_by_step(chest_size, 34, 53, 3)
    else:
        return 0


def get_shirt_size_by_step(chest_size, min, max, step):
    '''
    Function -- get_shirt_size_by_step
    Parameters:
    chest_size -- customer's input
    min -- minimum available number for such type
    max -- maximum available number for such type
    step -- step between each size
    Returns:
    using the result of "steps" to get shirt size
    '''
    if chest_size < min or chest_size >= max:
        return "not available"

    relative_size = chest_size - min
    steps = relative_size // step
    if steps == 0:
        return "S"
    elif steps == 1:
        return "M"
    elif steps == 2:
        return "L"
    elif steps == 3:
        return "XL"
    elif steps == 4:
        return "XXL"
    else:
        return "XXXL"


def main():
    chest_size = float(input("Chest measurement in inches: "))

    if check_input_valid(chest_size):
        print("Your size choices:")
        print("Kids size: " + get_shirt_size(chest_size, 'k'))
        print("Womens size: " + get_shirt_size(chest_size, 'w'))
        print("Mens size: " + get_shirt_size(chest_size, 'm'))
    else:
        print("Sorry, we don't carry your size")


if __name__ == "__main__":
    main()
