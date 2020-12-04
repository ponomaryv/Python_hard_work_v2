# Problem Set 2, hangman.py
# Name: Oleksandr Ponomaryv ,KM-03
# Collaborators: Anton Mitchenko(KM-03) , Petrychenko Nikita(Km-01)
# Time spent:2 night

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
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

# end of helper code

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
    pass



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    pass



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    pass
    
    

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
    tries = 6
    warnings = 3
    letters = set()
    result = get_guessed_word(secret_word, letters)
    print(f'I am thinking of a word that is {len(secret_word)} letters long')
    print(f'Ur have {warnings} warnings')
    while tries > 0 and (not is_word_guessed(secret_word, letters)):

        print('-' * 12)
        print(f'You have {tries} guesses left.\nAvailable letters: {get_available_letters(letters)}')
        let = input('Please guess a letter:')
        if hints and let == "*":
            show_possible_matches(result)
        elif let in letters:  #
            warnings -= 1
            print(f"Oops! You've already guessed that letter. You now have {max(0, warnings)} warnings: {result}")  #
        elif not let.isalpha():  #
            warnings -= 1
            print(f'Oops! That is not a valid letter. You have {max(0, warnings)} warnings: {result}')
        else:  #
            letters.add(let)
            result = get_guessed_word(secret_word, letters)

            if let in secret_word:  #
                print(f'Good guess: {result}')
            else:  #
                tries -= 1
                if let in {'a', 'o', 'e', 'i', 'u'}:
                    tries -= 1
                print(f'Oops! That letter is not in my word')
        if warnings < 0:
            tries += warnings
            warnings = 0

    if tries <= 0:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}')
    else:
        points = int(tries) * len(set(secret_word))
        print(f'Congratulations, you won! Your total score for this game is: {points}')



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
    pass


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    pass


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
    pass




if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
