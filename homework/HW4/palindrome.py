'''
Fall2020
CS 5001 HW3
Yici Zhu
it's a program to check if a word is palindrome
'''


def is_palindrome(word):
    '''
    Function -- is_palindrome
    to check if a word is palindrome
    Parameters:
    word-- user input
    Returns:
    if it's a palindrome, return true, else return false
    '''
    word_val = word.lower()
    word_val = word_val.replace(" ", "")
    if len(word_val) > 1 and word_val[0:] == word_val[::-1]:
        return True
    else:
        return False


def main():
    word = input("is_palindrome:")
    if is_palindrome(word) is True:
        print("# True")
    else:
        print("# False")


if __name__ == "__main__":
    main()
