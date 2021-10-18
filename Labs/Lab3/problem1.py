def splited_amount(total_amount, people, tip):
    splited_amount = (total_amount / people) * tip + (total_amount / people)
    return splited_amount

def main():
    total_amount = float (input ("what is the total amount of your bill?"))
    people = int (input ("how many people will split the bill?"))
    tip = float (input ("the percentage everyone willing to tip?"))

    bill = splited_amount(total_amount, people, tip)

    print(bill)


if __name__ == "__main__":
    main()