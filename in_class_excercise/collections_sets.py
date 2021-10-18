'''
Sample Code
CS 5001, Fall 2020, Lecture 8

This sample code shows how to work with Python sets.
'''


def main():
    print("Working with sets")
    # Sets - Unordered, mutable. Created using {} or set()
    avengers = {"Captain America", "Iron Man", "Hulk", "Thor", "Black Widow"}
    thor_family = {"Thor", "Loki", "Odin"}

    # Access items by iterating or searching
    for character in avengers:
        print(character, "is an Avenger")

    # Add items to a set using .add()
    # TODO: Add "Blank Panther" and "Captain Marvel" to the avengers
    avengers.add("Black Panther")
    avengers.add("Caprain Marvel")
    print(avengers)

    # Perform operations on multiple sets e.g. union, intersection, difference
    # TODO: Use a set method to find the members of thor_family that are also in avengers. Should just be Thor.
    print(avengers.intersection(thor_family))

    # TODO: Use a set method to find the members of avengers that are NOT in thor_family. Should be everyone except Thor.
    print(avengers.difference(thor_family))
    print(avengers - thor_family)


if __name__ == "__main__":
    main()
