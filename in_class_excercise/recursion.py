def factorial(number):
    if number == 0 or number == 1:
        return 0
    else:
        return number * factorial(number - 1)

def multiplication(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    else:
        return x + multiplication(num1, num2 - 1)


def sum_list(lst):
    #two recursive functions
    #sum the total of each inner list, inner for loop
    #sum the total,outer for loop
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

def sum_nested_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return sum_list(lst[0]) + sum_nested_list(lst[1:])


