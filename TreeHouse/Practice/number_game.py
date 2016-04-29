#! /usr/bin/python
# _*_coding: utf-8

import random


def game():
    # generate a radom number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []

    # limit guesses
    while len(guesses) < 5:
        try:
            # get a number guess from play
            # safely make an int
            guess_num = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number!".format(guess_num))
        else:
            # compare guess and secret number
            if guess_num == secret_num:
                print("You got it! My number is: {}".format(secret_num))
                break
            elif secret_num > guess_num:
                # too high message
                print("My number is higher than {}".format(guess_num))
            else:
                # too low message
                print("My number is lower than {}".format(guess_num))
            guesses.append(guess_num)

    else:
        print("You do not get it! My number is {}".format(secret_num))
    # play again
    play_again = input("Do you want to play again? Y/N > ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")

game()
