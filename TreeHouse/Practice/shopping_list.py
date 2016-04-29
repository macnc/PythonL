#! /usr/local/bin/python3
# _*_coding: utf-8

# Make a list to hold on our items
shopping_list = []

# print out instruction on how to use the app
print("What should we pick up at the store?")
print("Enter 'done' to stop adding items")

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == "done":
        break

    # add new items to our list
    shopping_list.append(new_item)

# print out the list
print("Here's your list")

for item in shopping_list:
    print(item)
