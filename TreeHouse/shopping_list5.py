#! /usr/bin/python
# _*_coding: utf-8

import sys
import os

shopping_list = []


# Show help message
def show_help():
    print(" **Separate each item with comma.")
    print(" **Type DONE to quit, SHOW to see the current list, REMOVE to "
          "delete the item, and HELP to get this message.")


# Show all of content in the shopping list
def show_list():
    count = 1
    for item in shopping_list:
        print("{}: {}".format(count, item))
        count += 1


def remove_item(idx):
    index = idx - 1
    item = shopping_list.pop(index)
    print("Remove {}.".format(item))


print("Please give me a list of things you want to shop for: ")
show_help()

while True:
    new_stuff = input("> ")

    if new_stuff == "DONE":
        print("\nHere's you list:")
        show_list()
        break
    elif new_stuff == "HELP":
        show_help()
        continue
    elif new_stuff == "SHOW":
        show_list()
        continue
    elif new_stuff == "REMOVE":
        show_list()
        idx = input("Which item? Tell me the number")
        remove_item(int(idx))
        continue
    else:
        new_list = new_stuff.split(",")
        index = input("Add this at a certain spot? Press enter for"
                      "the end of list, or give me a number. Currently "
                      "{} items in the list. ".format(len(shopping_list)))

        if index:
            spot = int(index) - 1
            for item in new_list:
                shopping_list.insert(spot, item.strip())
                spot += 1
        else:
            for item in new_list:
                shopping_list.append(item.strip())
