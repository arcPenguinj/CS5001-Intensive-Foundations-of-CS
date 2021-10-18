def avaverage(scorelist):
    count = 0
    sumscore = 0
    while count < len(scorelist):
        sumscore = sumscore + scorelist[count]
        count += 1
    avaverage = sumscore / len(scorelist)
    return avaverage

def median(scorelist):
    scorelist.sort()
    if len(scorelist) % 2 == 0:
        median1 = len(scorelist) / 2 - 1
        median2 = len(scorelist) / 2
        median = (scorelist[median1] + scorelist[median2]) / 2
    else:
        median_index = len(scorelist) // 2
        median = scorelist[median_index]
    return median

def lowest_score(scorelist):
    count = 1
    lowest = scorelist[0]
    while count < len(scorelist):
        if lowest > scorelist[count]:
            lowest = scorelist[count]
        count += 1
    return lowest


def main():
    scorelist = [98, 88, 89, 97, 78, 99, 59, 85, 92, 74, 79]
    avaverage_score = avaverage(scorelist)
    print("Average:", avaverage_score)
    median_score = median(scorelist)
    print("Median:", median_score)
    lowestscore = lowest_score(scorelist)
    print("the lowest score:", lowestscore)


main()