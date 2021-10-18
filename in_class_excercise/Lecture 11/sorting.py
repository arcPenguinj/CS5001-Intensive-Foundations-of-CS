'''
Sample Code
CS 5001, Fall 2020 - Lecture 11

Implementations of two famous sorting algorithms: bubble sort and merge sort.
'''


def bubble_sort(lst):
    '''
        Function -- bubble_sort
            Sorts a list using the bubble sort algorithm.
        Parameter:
            lst -- The list to sort.
        Returns:
            Nothing. Lists are mutable so the list is sorted in place.
    '''
    length = len(lst)
    for iteration in range(length):
        max_pos = length - iteration - 1
        for left_item in range(max_pos):
        # If the item on the left is bigger...
            right_item = left_item+1
            if lst[left_item] > lst[right_item]:
                # Swap the items
                temp = lst[left_item]
                lst[left_item] = lst[right_item]
                lst[right_item] = temp


def merge_sort(lst):
    '''
        Function -- merge_sort
            Sorts a list using the merge sort algorithm.
        Parameter:
            lst -- The list to sort.
        Returns:
            Nothing. Lists are mutable so the list is sorted in place.
    '''
    if len(lst) > 1:
        # Find the mid point
        mid = len(lst) // 2
        # Split
        left_half = lst[:mid]
        right_half = lst[mid:]
        
        # Recursively call merge_sort on each half
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge the two halves
        merge(lst, left_half, right_half)


def merge(lst, left, right):
    '''
        Function -- merge
            Helper function that performs the merge step of merge sort.
        Parameters:
            lst -- the list to merge into
            left -- the left half of the list to merge
            right -- the right half of the list to merge.
        Returns:
            Nothing. Lists are mutable so the merged list will be accessible
            without returning it.
    '''
    i = 0 # Our position in the left list
    j = 0 # Our position in the right list
    k = 0 # Our position in lst
  
    # As long as there are items in left AND right
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1
    
    # If only the left list has items
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1
    
    # if only the right list has items
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1


def main():
    desserts = ["carrot", "banana", "pecan", "apple", "pumpkin"]
    merge_sort(desserts)
    print("Sorted desserts =", desserts)


if __name__ == "__main__":
    main()