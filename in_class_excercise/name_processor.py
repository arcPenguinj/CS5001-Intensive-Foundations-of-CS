'''def main():
    highest = None
    i = 0
    while i < 10:
        user_input = int(input("Enter an integer: "))
        if highest is None or highest < user_input:
            highest = user_input
        i += 1
    print("The highest number is: ", highest)

if __name__ == "__main__":
    main()
'''
'''
def est_to_pst(time_pst):
    hr = int(time_pst[0:2])
    hr = hr -3
    if hr < 0:
        hr = 24 + hr
    additional_zero = ""
    if hr < 10:
        additional_zero = "0"
    return additional_zero + str(hr) + time_pst[2:]

def main():
    question1 = input("what time is it in EST: ")
    print(est_to_pst(question1))


if __name__ == "__main__":
    main()
'''
'''
def pst_to_est(time_pst):
    hr = int(time_pst[0:2])
    est = hr + 3
    additional_zero = ""
    if est >= 24:
        est = est - 24
    if est < 10:
        additional_zero = "0"
    return additional_zero + str(est) + time_pst[2:]

def main():
    question1 = input("what time is it in PST: ")
    print(pst_to_est(question1))


if __name__ == "__main__":
    main()
'''

'''
def main():
    i = 0
    lst = []
    while i < 10:
        x = int(input("Enter an integer:"))
        lst.append(x)
        i += 1
    sort = sorted(lst)
    print(sort[0])

if __name__ == "__main__":
    main()
'''
'''
def main():
    i = 0
    lowest = None
    while i < 10:
        inputs = int(input("Enter an integer:"))
        if lowest is None or lowest > inputs:
            lowest = inputs
        i += 1
    return print(lowest)


if __name__ == "__main__":
    main()

'''

'''
def get_ticket_cost(group_ages):
    totalprice = 0
    for i in group_ages:
        if i < 15:
            price = 20 * 0.5
        elif i >= 60:
            price = 20 * 0.75
        else:
            price = 20
        totalprice +=price
    return totalprice

def main():
    print(get_ticket_cost([10, 39, 40, 50]))


if __name__ == "__main__":
    main()
'''


def name_processor(old_list):
    new_list = []
    i = 0
    while i < len(old_list):
        name = old_list[i].split(" ")
        if len(name) <= 1:
            new_list.append(name[0])
        elif len(name) >= 2:
            name = name[-1] + ", " + name[0]
            new_list.append(name)
        i += 1
    return new_list

def main():
    old_list = ["Pele", "Sarah Jessica Parker", "Darth Vader", ""]
    print(name_processor(old_list))


if __name__ == "__main__":
    main()