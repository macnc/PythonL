#! /usr/bin/python
# _*_coding: utf-8


def show_help():
    # print out instructions on how to use the app
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")


def show_list(shopping_list):
    # print out the list
    print("Here's your list:")

    for item in shopping_list:
        print(item)


def add_to_list(shopping_list, new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item,
                                                    len(shopping_list)))
    return shopping_list


def main():
    show_help()
    # make a list to hold onto our items
    shopping_list = []

    while True:
        # ask for new items
        new_item = input("> ")

        # be able to quit the app
        if new_item == 'DONE':
            break
        elif new_item == 'HELP':
            show_help()
            continue
        elif new_item == 'SHOW':
            show_list(shopping_list)
            continue
        add_to_list(shopping_list, new_item)

    show_list(shopping_list)

main()
