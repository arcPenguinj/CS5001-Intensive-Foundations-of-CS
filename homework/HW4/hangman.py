'''
Fall2020
CS 5001 HW3
Yici Zhu
it's a program for hangman game
'''


def generate_word(word, guessed_list):
    '''
    Function -- generate_word
    To create a placeholder
    Parameters:
    word--secrert word
    guessed_list -- letters guessed by the player
    Returns:
    return the secret word with all letters except
    any the user has correctly guessed replaced by underscores
    '''
    placeholder = ""
    count = 0
    while count < len(word):
        if word[count] in guessed_list:
            placeholder = placeholder + word[count]
        else:
            placeholder = placeholder + "_"
        count += 1
    return placeholder


def main():
    game_word = ["APPLE", "OBVIOUS", "XYLOPHONE"]
    rounds = 0
    win = 0
    total_rounds = 3
    while rounds < total_rounds:
        # win += run_game(game_word[rounds])
        guessed = ""
        tries = 6
        firstTime = True
        word = game_word[rounds]
        while tries > 0:
            print(generate_word(word, guessed))
            if not firstTime:
                print("Your guesses so far:", guessed)
            firstTime = False
            guess_letter = input("Enter a letter or word: ").upper()
            if len(guess_letter) == 1:
                if guess_letter in guessed:
                    print("You've already guessed that letter!")
                elif guess_letter not in guessed:
                    guessed = guessed + guess_letter
                    tries -= 1
            elif len(guess_letter) > 1:
                if guess_letter == word:
                    print("You win!")
                    win += 1
                    break
                # else: meaning guessed word is wrong, back to while loop
        if tries == 0:
            print("You lose! The word was " + word)
        rounds += 1
    print("You won " + str(win) + " out of 3")


if __name__ == "__main__":
    main()
