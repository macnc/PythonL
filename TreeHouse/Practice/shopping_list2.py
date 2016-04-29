#! /usr/local/bin/python3
# _*_coding: utf-8

# have a HELP command
# have a show command
# clean code up in general

# Make a list to hold on our items
shopping_list = []


def show_help():
    # print out instruction on how to use the app
    print("What should we pick up at the store?")
    print('''
          Enter 'done' to stop adding items
          Enter 'HELP' for this help
          enter 'show' to see your current list
          ''')


def show_list():
    # print out the list
    print("Here's your list")

    for item in shopping_list:
        print(item)


def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item,
                                                    len(shopping_list)))

show_help()
while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == "done":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "show":
        show_list()
        continue
    add_to_list(new_item)

show_list()
