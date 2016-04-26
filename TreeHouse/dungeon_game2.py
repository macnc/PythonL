#! /usr/bin/python
# _*_coding: utf-8

import sys
import os
import random


def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def start_position_characters(nr_cells_hor, nr_cells_ver):
    # Go on randomly selecting the starting positions until they are all
    # different from each other.
    tupple_h = ("H", random.randint(0, nr_cells_hor-1),
                random.randint(0, nr_cells_ver-1))
    tupple_m = ("M", random.randint(0, nr_cells_hor-1),
                random.randint(0, nr_cells_ver-1))
    tupple_d = ("D", random.randint(0, nr_cells_hor-1),
                random.randint(0, nr_cells_ver-1))
    spc = [tupple_h, tupple_m, tupple_d]
    while (((spc[0])[1] == (spc[1])[1]) and ((spc[0])[2] == (spc[1])[2])) or
    (((spc[0])[1] == (spc[2])[1]) and ((spc[0])[2] == (spc[2])[2])) or
    (((spc[1])[1] == (spc[2])[1]) and ((spc[1])[2] == (spc[2])[2])):
            start_position_characters(nr_cells_hor, nr_cells_ver)
    else:
        return(spc)


def create_grid_input(characters, x_as, y_as):
    x_list = list(range(0, x_as))
    grid_list = []
    for waarde in x_list:
        y_count = 0
        while y_count < y_as:
            if waarde == (characters[1])[2] and y_count == (characters[1])[1]:
                # M
                grid_tuple = waarde, y_count, (characters[1])[0]
                grid_list.append(grid_tuple)
            elif waarde == (characters[2])[2] and y_count ==
            (characters[2])[1]:
                # D
                # grid_tuple = waarde, y_count, (characters[2])[0] This line
                # if the Door must be visible!
                grid_tuple = waarde, y_count, "."
                grid_list.append(grid_tuple)
            elif waarde == (characters[0])[2] and
            y_count == (characters[0])[1]:
                grid_tuple = waarde, y_count, (characters[0])[0]
                grid_list.append(grid_tuple)
            else:
                grid_tuple = waarde, y_count, "."
                grid_list.append(grid_tuple)
            y_count += 1
    for extra_character in characters:
        if extra_character[0] not in ("H", "M", "D"):
            # Character = "*" (for the 'bread crumbs').
            # In the 'original drawing' these cases are still a "."
            try:
                bread_crumb_index = grid_list.index((extra_character[2],
                                                     extra_character[1], "."))
                # Find the index of 'drawing' .-tuples with the same
                # coördinates as the 'real' *-tuples (in characters).
                grid_list[bread_crumb_index] = (extra_character[2],
                                                extra_character[1], "*")
                # Change for those cases the "." into a "*".
            except:
                # The try/except is because a "M" can 'overwrite'
                # the position of a *-tuple
                grid_list
    return(grid_list)


def draw_grid(cells):
    right_row_cell = "|"
    row_number_old = 0
    for tupple in cells:
        bulk_row_cell = "|{}".format(tupple[2])
        row_number_current = tupple[0]
        if row_number_current != row_number_old:
            print(right_row_cell)
            print(bulk_row_cell, end='')
        else:
            print(bulk_row_cell, end='')
        row_number_old = row_number_current
    print(right_row_cell)
    print('')
    return()


def move_options_human(old_position_characters, nr_cells_hor, nr_cells_ver):
    for character in old_position_characters:
        move_options = []
        if character[0] == "H":
            if character[1] == 0:
                move_options.append("RIGHT")
            elif character[1] == nr_cells_ver-1:
                move_options.append("LEFT")
            else:
                move_options.append("RIGHT")
                move_options.append("LEFT")
            if character[2] == 0:
                move_options.append("DOWN")
            elif character[2] == nr_cells_hor-1:
                move_options.append("UP")
            else:
                move_options.append("DOWN")
                move_options.append("UP")
            break
    print(move_options)
    return()


def move_options_monster(old_position_characters, nr_cells_hor, nr_cells_ver):
    for character in old_position_characters:
        move_options = []
        if character[0] == "M":
            if character[1] == 0:
                move_options.append("RIGHT")
            elif character[1] == nr_cells_ver-1:
                move_options.append("LEFT")
            else:
                move_options.append("RIGHT")
                move_options.append("LEFT")
            if character[2] == 0:
                move_options.append("DOWN")
            elif character[2] == nr_cells_hor-1:
                move_options.append("UP")
            else:
                move_options.append("DOWN")
                move_options.append("UP")
            break
    return(move_options)


def random_select_move_monster(old_position_characters,
                               nr_cells_hor, nr_cells_ver):
    move_options_monster_var = move_options_monster(old_position_characters,
                                                    nr_cells_hor, nr_cells_ver)
    move_monster = random.choice(move_options_monster_var)
    return(move_monster)


def new_position_characters(old_position_characters, nr_cells_hor,
                            nr_cells_ver):
    input_move_human =
    input("In which direction do you want "
          "to move (type EXIT to quit)?").upper()
    while input_move_human not in ("UP", "DOWN", "LEFT", "RIGHT", "EXIT"):
        print("You didn't enter a correct move!")
        input_move_human = input("In which direction do you"
                                 " want to move (type EXIT to quit)? ").upper()
    input_move_monster = step_monster(old_position_characters,
                                      nr_cells_hor, nr_cells_ver)
    new_position_human = ()
    new_position_monster = ()
    for character in old_position_characters:
        if character[0] == "H":
            # Focus on Human.
            if input_move_human == "EXIT":
                sys.exit()
            if input_move_human == "UP":
                new_position_human = ("H", character[1], character[2]-1)
            elif input_move_human == "DOWN":
                new_position_human = ("H", character[1], character[2]+1)
            elif input_move_human == "LEFT":
                new_position_human = ("H", character[1]-1, character[2])
            elif input_move_human == "RIGHT":
                new_position_human = ("H", character[1]+1, character[2])
        if character[0] == "M":
            # Focus on Monster.
            if input_move_monster == "UP":
                new_position_monster = ("M", character[1], character[2]-1)
            elif input_move_monster == "DOWN":
                new_position_monster = ("M", character[1], character[2]+1)
            elif input_move_monster == "LEFT":
                new_position_monster = ("M", character[1]-1, character[2])
            elif input_move_monster == "RIGHT":
                new_position_monster = ("M", character[1]+1, character[2])
        new_positions_output = [new_position_human, new_position_monster]
    return(new_positions_output)

# Add a 'bread crumbs' (with sign "*") to the 'original signs'
# ("H", "M" and "D" [and later on also "*"]).
# Copy the H-tuple and replace the "H" for a "*" to get the *-tuple
# on the 'old coördinates' of the H-tuple.
# Put the new *-tuple (everytime) directly after the H", "M" and "D" in
# the list (not for a drawing purpose, but because that is the most easy).
# The new H-tuple 'comes in' through the call to new_position_characters.


def add_bread_crumb(old_position_characters, nr_cells_hor, nr_cells_ver):
    new_position_characters_var = absnew_position_characters
    (old_position_characters, nr_cells_hor, nr_cells_ver)
    bread_crumb = old_position_characters[0]
    bread_crumb = '*', bread_crumb[1], bread_crumb[2]
    del old_position_characters[0:2]
    next_position_characters = old_position_characters
    next_position_characters.insert(0, new_position_characters_var[1])
    next_position_characters.insert(0, new_position_characters_var[0])
    next_position_characters.insert(3, bread_crumb)
    return(next_position_characters)


def step_human(old_position_characters, nr_cells_hor, nr_cells_ver):
    cells = create_grid_input(old_position_characters,
                              nr_cells_hor, nr_cells_ver)
    draw_grid(cells)
    move_options_human(old_position_characters, nr_cells_hor, nr_cells_ver)
    next_position_characters = add_bread_crumb(old_position_characters,
                                               nr_cells_hor, nr_cells_ver)
    return(next_position_characters)


def step_monster(old_position_characters, nr_cells_hor, nr_cells_ver):
    move_monster = random_select_move_monster(old_position_characters,
                                              nr_cells_hor, nr_cells_ver)
    return(move_monster)


def walk_human(nr_cells_hor, nr_cells_ver):
    initial_position_characters = start_position_characters(nr_cells_hor,
                                                            nr_cells_ver)
    npc = step_human(initial_position_characters, nr_cells_hor, nr_cells_ver)
    while True:
        if ((npc[0])[1] == (npc[1])[1]) and ((npc[0])[2] == (npc[1])[2]):
            cells = create_grid_input(npc, nr_cells_hor, nr_cells_ver)
            draw_grid(cells)
            print("You lose, you have been eaten by the Monster!")
            break
        elif ((npc[0])[1] == (npc[2])[1]) and ((npc[0])[2] == (npc[2])[2]):
            cells = create_grid_input(npc, nr_cells_hor, nr_cells_ver)
            draw_grid(cells)
            print("You win, you have escaped through the Door!")
            break
        else:
            npc = step_human(npc, nr_cells_hor, nr_cells_ver)
    return()


def main():
    clear()
    nr_cells_hor = int(input("How many rooms must there be horizontally? "))
    nr_cells_ver = int(input("How many rooms must there be vertically? "))
    walk_human(nr_cells_hor, nr_cells_ver)
    return()

main()
