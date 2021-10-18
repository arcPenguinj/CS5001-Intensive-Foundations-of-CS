'''
Fall2020
CS 5001 HW5
Yici Zhu
it's a program checking upc number
'''


def is_valid_upc(upc_num):
    '''
    function -- is_valid_upc
    count from right to left, leave the digit on even
    position, multiply digits in odd position by 3,
    and sum the result, if sum is a number multiple of 10,
    it's valid upc, otherwise, it's not.
    parameter -- upc_num, the string to check
    return: True if the string is upc number, False
    if it is not a valid upc number
    '''
    if not upc_num.isnumeric():
        return False
    sum = 0
    count = 0
    i = -1
    multiplier = 3
    divisor = 10
    for i in range(-1, 0 - len(upc_num) - 1, -1):
        if count % 2 == 0:
            sum += int(upc_num[i])
        else:
            sum += int(upc_num[i]) * multiplier
        count += 1
    if sum % divisor == 0:
        return True
    else:
        return False
