#! /usr/bin/python
# _*_coding: utf-8

# Create a function named word_count() that takes a string. Return a dictionary
# with each word in the string as the key and the number of times it appears as
# the value.


# E.g. word_count("I am that I am") gets back a dictionary like:
# {'i': 2, 'am': 2, 'that': 1}
def word_count(words):
    # Using .split() on the sentence will give you a list of words.
    words = words.split(“ ”)
    status = {}
    # In a for loop of that list, you'll have a word that you can
    for word in words:
        # Lowercase the string to make it easier.
        word_l = word.lower()
        # check for inclusion in the dict
        # (with "if word in dict"-style syntax).
        if word_l in status:
            # if the word exist, update the value of the key
            status[word_l] += 1
            # Or add it to the dict with something like word_dict[word] = 1.
            else:
                status.update({word_l: 1})
    return status

# Let's test the function
word = input("Please say somehing as your input. > ")
word_count(word)
