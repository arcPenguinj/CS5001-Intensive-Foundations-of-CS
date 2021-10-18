'''
Yici Zhu
Fall 2020
CS5001 Lab 4
'''


def log(number):
    loops = 0
    num = 1
    while num != number:
        num = num * 2
        loops += 1
    return loops


def factorial(number):
    steps = 1
    num = 1
    while steps <= number:
        num = num * steps
        steps += 1
    return num


def main():
    question = int(input("Enter a positive integer:"))
    print(log(question))
    question2 = int(input("Enter the number you want to calculate factoria: "))
    print(factorial(question2))


if __name__ == "__main__":
    main()
