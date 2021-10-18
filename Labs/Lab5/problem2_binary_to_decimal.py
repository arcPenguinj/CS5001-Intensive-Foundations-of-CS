def bi_to_de(binarynumber):
    count = -1
    power = 0
    decimal = 0
    while -count <= len(binarynumber):
        decimal = decimal + int(binarynumber[count]) * (2 ** power)
        power += 1
        count -= 1
    return decimal


def main():
    binarynumber = input("Enter a binary number")
    print(bi_to_de(binarynumber))

main()