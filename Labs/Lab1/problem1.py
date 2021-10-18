def main ():
    total_amount = float (input ("what is the total amount of your bill?"))
    people = int (input ("how many people will split the bill?"))
    tip = float (input ("the percentage everyone willing to tip?"))

    amount = (total_amount / people) * tip + (total_amount / people)

    print ("the number is:" + str(amount))
    #....

if __name__ == "__main__":
    main()

