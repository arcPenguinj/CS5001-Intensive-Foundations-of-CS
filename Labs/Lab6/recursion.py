def GCD(a, b):
    if a == 0:
        return b
    if a > b:
        return GCD(b, a) # so that we can always assume a <= b

    r = b % a
    return GCD(r, a)

# print(GCD(270, 192))
# print(GCD(0, 4))
# print(GCD(12, 8))
# print(GCD(15, 30))

def GCD_new(list):
    if len(list) == 0:
        return 0 # invalid case
    if len(list) == 1:
        return list[0]
    a = list[0]
    b = list[1]
    gcd = GCD(a, b)
    return GCD_new([gcd] + list[2:])

print(GCD_new([1619, 14038]))
# print(GCD_new([270, 192, 12, 0]))
# print(GCD_new([270, 8, 2, 3]))

'''
def logarithm(n):
    if n == 0:
        return 0 # invalid case
    if n == 1:
        return 0
    return 1 + logarithm(n//2)

# print(logarithm(32))
# print(logarithm(1))
# print(logarithm(1024))
# print(logarithm(5))

def b2d(num):
    if len(num) == 0:
        return 0
    last_digit = int(num[-1])
    return last_digit + 2 * b2d(num[0:len(num)-1])

# print(b2d('1010'))
# print(b2d('1'))
# print(b2d(''))
# print(b2d('111'))
'''