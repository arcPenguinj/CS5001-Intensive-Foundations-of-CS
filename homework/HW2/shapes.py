'''
Fall2020
CS 5001 HW2
Yici Zhu
it's a program for calculate area of shapes
'''


def main():
    shape = input("Select a shape (triangle, square, or rectangle): ")

    shapeval = shape.lower()

    if shapeval == "triangle":
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
    elif shapeval == "rectangle":
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
    elif shapeval == "square":
        width = float(input("Enter the width: "))
        height = width
    else:
        print('Unknown shape')
        return

    if width <= 0:
        print("Invalid width")
        return
    if height <= 0:
        print("Invalid height")
        return

    if shapeval == "triangle":
        area = format(round(width * height / 2, 2), '.2f')
    elif shapeval == "rectangle":
        area = format(round(width * height, 2), '.2f')
    elif shapeval == "square":
        area = format(round(width ** 2, 2), '.2f')

    print("The area of the " + str(shapeval) + " is " + str(area))


if __name__ == "__main__":
    main()
