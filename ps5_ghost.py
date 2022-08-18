# Problem Set 5: Ghost
# Name: Jafar Bakhshaliyev


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

    inFile = open(WORDLIST_FILENAME, 'r')
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def isvalid_letter(letter):
    """
    This function checks if validity of letter by looking at ASCII Letters.
    :param letter: str
    :return: boolean
    """
    isval_letter = True
    if len(letter) != 1: isval_letter = False
    if letter.lower() not in string.ascii_letters: isval_letter= False;
    return isval_letter


def update_word(word, letter):
    """
    This function takes word and letter, then returns an updated word
    by adding letter to the end of word.
    :param word: str
    :param letter: str
    :return: str
    """
    word += letter
    return word


def isvalid_word(word):
    """
    This function takes a word and check if there is a real word
    starts with that input word.
    :param word: str
    :return: boolean
    """
    isval_word = False
    for wrd in wordlist:
        if wrd.startswith(word.lower()): isval_word = True
    return isval_word


def isWord(word):
    """
    This function takes a word and checks if word exists in the wordlist.
    (Checks any player can form actual word.)
    :param word: str
    :return: boolean
    """
    is_in_wordlist = False
    if word.lower() in wordlist: is_in_wordlist = True
    return is_in_wordlist


def play_one(wordlist):
    """
    This function takes wordlist and starts one game for Ghost.
    """
    print('Welcome to Ghost!')
    print('Player 1 goes first.')
    word = ''
    print('Current word fragment:', word)
    count = 1
    while True:
        if count % 2 != 0:
            letter = input('Player 1 says letter:')
            print()
        else:
            letter = input('Player 2 says letter:')
            print()
        if isvalid_letter(letter):
            word = update_word(word, letter)
            print('Current word fragment:', word)
            count += 1
        else:
            print('Invalid letter!')
        if not isvalid_word(word):
            if count % 2 == 0:
                print(f'Player 1 loses because no word begins with {word} !')
                print('Player 2 wins!')
            else:
                print(f'Player 2 loses because no word begins with {word} !')
                print('Player 1 wins!')
            break
        if isWord(word) and len(word) > 3:
            if count % 2 == 0:
                print(f'Player 1 loses because {word} is a word!')
                print('Player 2 wins!')
            else:
                print(f'Player 2 loses because {word} is a word!')
                print('Player 1 wins!')
            break
        if count % 2 != 0:
            print('Player 1\'s turn')
        else:
            print('Player 2\'s turn')


def play_ghost(wordlist):
    """
    This is actual playing ghost game and it takes wordlist and asks you to
    play many times or just exit game.
    """
    while True:
        cmd = input('Enter n to start a new game or e to end game:')
        if cmd == 'n':
            play_one(wordlist)
            print()
        elif cmd == 'e':
            break
        else:
            print("Invalid command.")


if __name__ == '__main__':
    wordlist = load_words()  # do not change the name of wordlist!
    play_ghost(wordlist)
