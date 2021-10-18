def main():
    num1 = float(input("Enter a number:"))
    subtotal = num1
    while True:
        number2 = input("Enter the next step in the calculator:")
        if number2 == "q" or number2 == "Q":
            print("Total = ", subtotal)
            break
        op = number2[0]
        num2 = float(number2[2:])
        if op == "+":
            subtotal = subtotal + num2
        elif op == "-":
            subtotal = subtotal - num2
        elif op == "*":
            subtotal = subtotal * num2
        elif op == "/":
            subtotal = subtotal / num2
        print("subtotal = " + str(subtotal))

if __name__ == "__main__":
    main()