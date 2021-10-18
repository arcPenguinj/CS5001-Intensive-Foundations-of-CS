def value_counts(lst):
    a = {}
    for item in lst:
        if item not in a.keys():
            a[item] = lst.count(item)
    return a