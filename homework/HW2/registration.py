'''
Fall2020
CS 5001 HW2
Yici Zhu
it's a program for Course Registration
'''


def main():
    course = input("Enter a course number: ")
    hasprerequisite = False

    courseval = course.capitalize()
    courseval = courseval.replace(" ", "")

    if courseval == "X101":
        print("You have successfully registered for X101")
    elif courseval == "X102":
        print("You have successfully registered for X102")
    elif courseval == "B500":
        hasprerequisite = True
    elif courseval == "B525":
        hasprerequisite = True
    elif courseval == "B701":
        hasprerequisite = True
    else:
        print("Invalid course number")
        return

    if hasprerequisite:
        question1 = input("What grade did you get for X101? ")
        question2 = input("What grade did you get for X102? ")
        question1qualified = True
        question2qualified = True

        question1cap = question1.capitalize()
        question2cap = question2.capitalize()

        if question1cap == "A" or question1cap == "B":
            question1qualified = True
        else:
            question1qualified = False

        if question2cap == "A" or question2cap == "B" or question2cap == "C":
            question2qualified = True
        else:
            question2qualified = False

        if question1qualified and question2qualified:
            print("You meet all the prerequisites"
                  " and have successfully registered for " + str(courseval))
        else:
            print("You do not meet the prerequisites for " + str(courseval))


if __name__ == "__main__":
    main()
