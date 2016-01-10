#!/usr/bin/python2.7
# _*_coding: utf-8

ex25 = "ex25"

# Split the words from a integrated sentence.
def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

# This function will sort all of words which split from sentence.
def sort_words(words):
    '''Sorts the words'''
    return sorted(words)

# The function will print out the first word from a sentence.
def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)
    print word

# The function will print out
def print_last_word(words):
    """Print the last word after popping it off"""
    word = words.pop(-1)
    print word


def sort_sentences(sentence):
    """Takes in a full sentences and return the sorted words"""
    word = break_words(sentence)
    return sort_words(word)


def print_first_and_last(sentence):
    """Print the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sort the words then prints the first and last one"""
    words = sort_words(break_words(sentence))
    print_first_word(words)
    print_last_word(words)

    """Or you can implemented this function like this"""
    words = sort_sentences(sentence)
    print_first_word(words)
    print_last_word(words)

def help(ex25):

    help = """
    Welcome to Ex25 module!
    Here we will list all of the detail of help for functions:

    break_words(argv):
    \t1. The function is used for split words from a sentence which is as a parameter you want to split, and the function
    \t   will return a list variable which have all of words split from sentence parameter.
    \t2. Notice: argv as the parameter you input in the function should be a sentence.

    sort_words(argv):
    \t1. The function will help you sort all of words you input as a function parameter
    \t2. The parameter of function should be a String list type variable.

    print_first_word(argv):
    \t1. The function will print out the first word in the list variable you inputted as a parameter in the function.
    \t2. The data type of parameter variable for the function should be a String list data type.

    print_last_word(argv):
    \t1. The function will print out the last word in the list variable you inputted as a parameter in the function.
    \t2. Notice: The data type of the parameter for the function should be a String list data type.

    sort_sentence(argv):
    \t1. The function will split all of the words in the sentence you inputted as a parameter in the function first,
    \t   then put all of these words in a list variable. Third step, these word the list will be sorted as a new list.
    \t2. The function will return a list variable data to the command who called.
    \t3. Notice: The data type of parameter \'argv\' should be a String type.

    """
    if ex25 is not None:
        print help