'''
def main():
    rate = 0.78
    fee_rate = 0.05
    amount = float(input("Enter amount to convert in USD:"))
    amount = round(amount, 2)
    if amount < 100 or amount > 5000:
        print("Unable to convert that amount")
        return
    else:
        gbp_amount = amount * rate
        fee = amount * fee_rate
        print("amount to convert in USD: ", amount)
        print(str(amount) + " USD is " + str(gbp_amount) + " GBP")
        print("Fee: " + str(fee) + " USD")


if __name__ == "__main__":
    main()
'''

'''
def main():
    rate = 1.34
    fee_rate = 0.03
    amount = float(input("Enter amount to convert in CAD:"))
    if amount < 50 or amount > 1000:
        print("Unable to convert that amount")
        return
    else:
        usd_amount = round(amount / rate, 2)
        fee = round(usd_amount * fee_rate, 2)
        print(str(amount) + " CAD is " + str(usd_amount) + " USD")
        print("Fee: " + str(fee) + " USD")


if __name__ == "__main__":
    main()
'''
#instructor's answer
quarters = int(input("How many quarters do you want? "))
QUARTERS_IN_DOLLAR = 4
MIN_NUM = 20
MAX_NUM = 100
FEE = 0.02
if quarters < MIN_NUM or quarters > MAX_NUM:
  print("Unable to convert that amount!")
else:
  total = quarters / QUARTERS_IN_DOLLAR
  fee_amt = round(total * FEE, 2)
  print("{} quarters = ${:.2f}".format(quarters, total))
  print("Fee = ${:.2f}".format(fee_amt))
  print("Amount owed = ${:.2f}".format(total + fee_amt))