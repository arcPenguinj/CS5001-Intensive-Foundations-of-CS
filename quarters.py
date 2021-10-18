'''
def main():
    quarter_rate = 0.25
    fee_rate = 0.02
    amount = int(input("Number of quarters needed:"))
    if amount < 20 or amount > 100:
        print("Unable to provide that amount")
        return
    else:
        dollars = round(amount * quarter_rate, 2)
        fee = round(dollars * fee_rate, 2)
        total = round(dollars + fee, 2)
        print(str(amount) + " quarters = $" + str(dollars))
        print("Fee = $", str(fee))
        print("amount owed = $" + str(total))

if __name__ == "__main__":
    main()

'''

def main():
    quarter_rate = 0.25
    bonus_rate = 0.05
    amount = int(input("Number of quarters:"))
    if amount < 20 or amount > 200:
        print("Unable to accept that amount")
        return
    else:
        dollars = round(amount * quarter_rate, 2)
        bonus = round(dollars * bonus_rate, 2)
        total = round(dollars + bonus, 2)
        print(str(amount) + " quarters = $" + str(dollars))
        print("Bonus = $", str(bonus))
        print("Total deposit = $ " + str(total))

if __name__ == "__main__":
    main()