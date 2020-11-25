# Problem Set 2, hangman.py
# Name: Oleksandr Ponomaryv,KM-03
# Collaborators:Anton Mitchenko
# Time spent:2 night

# Hangman Game
# -----------------------------------
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# -----------------------------------

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    return letters_guessed in set(secret_word)


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    result = list(len(secret_word) * '_')
    for j in range(len(secret_word)):
        if secret_word[j] in letters_guessed:
            result[j] = secret_word[j]

    return ' '.join(result)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    return set('abcdefghijklmnopqrstuvwxyz') - set(letters_guessed)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    letters_guessed = []
    N_guesses = 6
    N_warnings = 3
    result = ''

    print('Hello in game in hangman!!!')

    while True:

        available_letters = ''.join(sorted(list(get_available_letters(letters_guessed))))

        print(f"""I am thinking of a word that is {len(secret_word)} letters long.
        You have {N_guesses} guesses left. Available letters: {available_letters}""")

        last_guessed = input(f'Enter the suggested letter:')
        last_guessed = last_guessed.lower()
        letters_guessed = letters_guessed + [last_guessed]

        result = get_guessed_word(secret_word, letters_guessed)

        if is_word_guessed(secret_word, last_guessed):
            if secret_word == ''.join(result.split(' ')):
                print(f'Congats!!! {N_guesses} guesses left! GG WP=)')
                print(f'{secret_word}')
                break
            else:
                print(f'Good guess: {result}')
        elif letters in list('abcdefghijklmnopqrstuvwxyz'):
            print(f'=( That letter is not in my word: {result}')
            if letters in "aeoiu":
                N_guesses -= 1
            N_guesses = N_guesses - 1
            if N_guesses <= 0:
                print(f'You loose, you have nothing guesses. Word was:')
                print(f'{secret_word}')
                break
            else:
                print('-' * 120)
                continue

        else:
            N_guesses = N_guesses - 1
            if N_warnings > 0:
                N_warnings = N_warnings - 1
                print(f'Oops! That is not a valid letter. You have {N_warnings} warnings left: {result}')
            else:
                print(f'Oops! Oops! Oops! Oops! Oops! Oops! Oops! Oops!')
                print(f'You loose, you have nothing. Word was:')
                print(f'{secret_word}')
                break

        if N_guesses < 0:
            print('You loose, you have nothing=( Word was:')
            print(f'{secret_word}')
            break

        print('-' * 20)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word = "".join(my_word.split())
    if len(my_word) == len(other_word):
        i = 0
        while i < len(my_word):
            if my_word[i] == "_":
                i += 1
            else:
                if my_word[i] != other_word[i]:
                    return False
                else:
                    i += 1
        return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = matches = [word for word in wordlist if match_with_gaps(my_word, word) == True]
    if not matches:
        print("No matches found.\n")
    else:
        print("Possible word matches are: " + ", ".join(matches), end="." + "\n")
    return


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''

    N_guesses = 6
    N_warning = 3
    Hints = 2
    letters_guessed = []
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    while True:
        available_letters = ''.join(sorted(list(get_available_letters(letters_guessed))))

        print(f"You have {N_guesses} guesses left.\t Available letters: {available_letters}")
        letters = input("Enter the suggested letter:  ")
        letters = letters.lower()
        letters_guessed = letters_guessed + [letters]
        result = get_guessed_word(secret_word, letters_guessed)

        if letters == "*":
            if Hints > 0:
                Hints = Hints - 1
                show_possible_matches(result)
                print('-' * 120)
            else:
                print("You are used all hints =(")
                N_guesses -= 1
                print('-' * 120)
                continue
        elif is_word_guessed(secret_word, letters):
            if secret_word == ''.join(result.split(' ')):
                print(f'Congats!!! {N_guesses} guesses left! GG WP=)')
                tprint(f'{secret_word}')
                break
            else:
                print(f'Good guess: {result}')
        elif letters in list('abcdefghijklmnopqrstuvwxyz'):
            print(f'=( That letter is not in my word: {result}')
            if letters in "aeoiu":
                N_guesses -= 1
            N_guesses = N_guesses - 1
            if N_guesses <= 0:
                print(f'You loose, you have nothing guesses. Word was:')
                print(f'{secret_word}')
                break
            else:
                print('-' * 120)
                continue
        else:
            if N_warning <= 0:
                N_guesses -= 1
            else:
                N_warning = N_warning - 1
                print(f"Oops! That is not a valid letter. You have {N_warning} warning left")
                print('-' * 120)
                if N_guesses <= 0:
                    print(f'You loose, you have nothing guesses. Word was:')
                    print(f'{secret_word}')
                    break
                else:
                    print('-' * 120)
                    continue



if __name__ == "__main__":


    secret_word = choose_word(wordlist)
    hangman(secret_word)

