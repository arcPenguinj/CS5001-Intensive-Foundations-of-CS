'''
Sample Code
CS 5001, Fall 2020 - Lecture 11

In-class algorithm timing exercise.
'''
import timeit # A module for "profiling" code
import random
from sorting import bubble_sort, merge_sort


def generate_list(n):
    '''
        Function -- generate_list
            Generates a list of size n. The list will contain all integers from
            0 to n-1 and will be shuffled.
        Parameter:
            n -- The length of the list.
        Returns:
            A list of size n.
    '''
    lst = [i for i in range(n)] # a "list comprehension"
    random.shuffle(lst)
    return lst


def main():
    '''
    Run this code 3 times with the following values of N:
    - 100
    - 1000
    - 10000
    '''
    N = 100 # This is the list length. 
    test_lst = generate_list(N)
    test_lst2 = test_lst.copy()

    setup = "from __main__ import bubble_sort, merge_sort, test_lst"

    print("Bubble sort results:")
    timeit.timeit("bubble_sort(test_lst)", setup=setup)


if __name__ == "__main__":
    main()