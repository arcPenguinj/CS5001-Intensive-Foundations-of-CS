'''
Sample Code
CS 5001, Fall 2020 - Lecture 11

An iterative implementation of binary search.
'''


def binary_search(item, lst):
    '''
        Function -- binary_search
            Perform a binary search for a given item. Return True when a
            matching item is found. Return False if no match is found.
        Parameters:
            item -- the item to search for.
            lst -- the list to search in.
    '''
    left_index = 0
    right_index = len(lst) - 1
    found = False
    
    while left_index <= right_index and not found:
        middle = (left_index + right_index) // 2
        if lst[middle] == item:
            found = True
        elif item < lst[middle]:
            # Search left
            right_index = middle - 1
        else:
            # Search right
            left_index = middle + 1
    return found


def main():
    desserts = ["apple", "banana", "carrot", "pecan", "pumpkin"]
    search1 = "pumpkin"
    search2 = "chocolate"
    search3 = "apple"

    print(binary_search(search1, desserts))
    print(binary_search(search2, desserts))
    print(binary_search(search3, desserts))


if __name__ == "__main__":
    main()