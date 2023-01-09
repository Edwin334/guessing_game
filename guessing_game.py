# Author: <Pinzhi Huang>
# Assignment #4 - Guessing Game
# Date due: 2021-11-11
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

####### DO NOT EDIT CODE BELOW (changing MAX_MISSES is ok) ########
import random
import sys

MAX_MISSES = 5
BORDER_LENGTH = 30
SINGLE_CHAR_LENGTH = 1

def blank_chars(word):
    """Returns a list of underscore characters with the same length as word.
    :param word: target word as a string
    :return: a list of underscore characters ('_') blank_chars("happiness")
    ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    """
    blank=[]
    for i in range(len(word)):
        blank.append("_")
    return blank

def space_chars(chars):
    """Returns a string with the characters in chars list separated by spaces.
    :param chars: a list of characters
    :return: a string containing characters in chars with intervening spaces
    >>> space_chars(['h', '_', 'p', 'p', '_', 'n', '_', '_', '_'])
    'h _ p p _ n _ _ _'
    """
    the_word=" ".join(chars)
    return the_word

def get_guess():
    """Prompts the user for a guess to check for the game's current word. When the user
    enters input other than a single character, the function prompts the user again
    for a guess. Only when the user enters a single character will the prompt for
    a guess stop being displayed. The function returns the single-character guess
    entered by the user.
    :return guess: a single character guessed by user
    """
    guess=input("Guess:\t")
    while not guess.isalpha() or len(guess)>1:
        guess = input("Guess:\t")
    return guess.lower()

def check_guess(word, guess):
    """Returns a list of positions where guess is present in word.
    An empty list should be returned when guess is not a single
    character or when guess is not present in word.
    :param word: target word as a string
    :param guess: a single character guessed by user
    :return positions: list of integer positions
    """
    lst=[]
    word_list=list(word)
    while guess in word_list:
        number=word_list.index(guess)
        lst.append(number)
        word_list[number]=" "
    return lst

def update_chars(chars, guess, positions):
    """Updates the list of characters, chars, so that the characters
    at the index values in the positions list are updated to the
    character guess.
    :param chars: a list of characters
    :param guess: a single character guessed by user
    :param positions: list of integer positions
    :return: None
    """
    for i in range(len(positions)):
        chars[positions[i]]=guess




def add_to_misses(misses, guess):
    """Adds the character guess to the misses list.
    :param misses: list of guesses not present in target word
    :param guess: a single character guessed by user
    :return: None
    """
    misses.append(guess)

def update_state(chars, misses, guess, positions):
    """Updates the state of the game based on user's guess. Calls the function update_chars() when
    the positions list is not empty to reveal the indices where the character guess is present. Calls the
    function add_to_misses() when the positions list is empty to add guess to the misses list.
    :param chars: a list of characters
    :param misses: list of guesses not present in target word
    :param guess: a single character guessed by user
    :param positions: list of integer positions
    :return: None
    """
    if positions ==[]:
        add_to_misses(misses, guess)
    else:
        update_chars(chars, guess, positions)

def is_round_complete(chars, misses):
    """Indicates whether or not a round has ended. This function returns True
    when the user has successfully guessed the target word or exceeds the
    number of allowed misses. Otherwise, the function returns False,
    indicating that the round is not complete. A message revealing the
    user's success or failure guessing the target word is output by this
    function when the round is complete.
    :param chars: a list of characters
    :param misses: list of guesses not present in target word
    :return status: True when round is finished, False otherwise
    """
    if len(misses) > MAX_MISSES:
        print()
        print("SORRY! NO GUESSES LEFT.")
        return True
    elif len(misses) <= MAX_MISSES and not "_" in chars:
        print()
        print("YOU GOT IT!")
        return True
    else:
        return False



def read_words(filepath):
    """Opens a file of word located at filepath, reads the file of words line by line,
    and adds each word from the file to a list. The list is returned by the
    function
    :param filepath: path to input file of words (one per line)
    :return word_list: list of strings contained in input file
    """
    f=open(filepath,"r")
    word=f.read()
    wordlist=word.split("\n")
    return wordlist

def get_word(words):
    """Selects a single word randomly from words list and returns it.
    :param words: list of strings
    :return word: string from words list
    """
    import random
    choice=random.randrange(len(words))
    word=words[choice]
    return word

def is_game_complete():
    """Prompts the user with "Play again (Y/N)?". The question is repeated
    until the user enters a valid response (one of Y/y/N/n). The function
    returns False if the user enters 'Y' or 'y' and returns True if the user
    enters 'N' or 'n'.
    :return response: boolean representing game completion status
    """
    choice=input("Play again (Y/N)? ")
    while choice != "Y" and choice != "y" and choice != "N" and choice != "n":
        choice = input("Play again (Y/N)? ")
    if choice == "Y" or choice=="y":
        return False
    elif choice=="N" or choice=="n":
        return True

def display_game_state(chars, misses):
    """
    Displays the current state of the game: the list of characters to display
    and the list of misses.
    """

    print()
    print('=' * BORDER_LENGTH)
    print()
    print("Word:\t{}\n".format(space_chars(chars)))
    print("Misses:\t{}\n".format("".join(misses)))


def run_guessing_game(words_filepath):
    """Controls running The Guessing Game. This includes parsing
    the words file and executing multiple rounds of the game.
    :param words_filepath: the location of the file of words for the game
    :return: None
    """
    try:
        temp=read_words(words_filepath)
    except IOError:
        print("The provided file location is not valid. Please enter a valid path to a file.")
    else:
        print("Welcome to The Guessing Game!")
        option=False
        while option != True:
            anwser=get_word(temp)
            misses=[]
            answer_list = blank_chars(anwser)
            while not is_round_complete(answer_list, misses):
                display_game_state(answer_list, misses)
                guess = get_guess()
                positions = check_guess(anwser, guess)
                update_state(answer_list, misses, guess, positions)
            display_game_state(anwser, misses)
            option = is_game_complete()
        print()
        print("Goodbye.")


####### DO NOT EDIT CODE ABOVE (changing MAX_MISSES is ok) ########

def main():

    ########## DO NOT EDIT ASSIGNMENT STATEMENT BELOW #########

    filepath = sys.argv[-1]
    run_guessing_game(filepath)

    ########## DO NOT EDIT ASSIGNMENT STATEMENT ABOVE #########

    # call run_guessing_game() with filepath as argument and remove pass below
    pass




if __name__ == '__main__':
    main()
