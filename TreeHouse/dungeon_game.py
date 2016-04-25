#! /usr/bin/python
# _*_coding: utf-8

# Please finish the homework for showing the monster's location
# 显示出怪兽的位置，这样就可以作弊啦，哈哈！

import random

CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]


def get_locations():
    # monster = random
    monster = random.choice(CELLS)
    # door = random
    door = random.choice(CELLS)
    # start = random
    start = random.choice(CELLS)

    # if monster, door, or start are the same, do it again
    if monster == door or monster == start or door == start:
        return get_locations()
        # return monster, door, start
    return monster, door, start


def draw_map(player):
    print(' _ _ _')
    tile = '|{}'

    for idx, cell in enumerate(CELLS):
        if idx in [0, 1, 3, 4, 6, 7]:
            if cell == player:
                print(tile.format('x'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == player:
                print(tile.format('x|'))
            else:
                print(tile.format('_|'))


def move_player(player, move):
    x, y = player

    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x += 1

    return x, y

    # Get the player's current location
    # If move is Left, y - 1
    # If move is Right, y + 1
    # If move is Up, x -1
    # If move is Down, x + 1
    return player


def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'DOWN', 'UP']
    # player = (x, y)

    # If player's y is 0, remove LEFT
    # If player's x is 0, remove UP
    # If player's y is 2, remmove RIGHT
    # If player's x is 2, remove DOWN
    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 2:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 2:
        moves.remove('DOWN')

    return moves


monster, door, player = get_locations()
print("Welcome to the dungeon!")

while True:
    moves = get_moves(player)
    # fill in player's position
    print("You're currently in room {}".format(player))
    # fill in with available moves
    draw_map(player)

    print("You can move {}".format(moves))
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    if move in moves:
        player = move_player(player, move)
    else:
        print('** Walls are hard, stop walking into them! **')
        continue

    if player == door:
        print('You escaped!')
        break
    elif player == monster:
        print('You ware eaten by the grue')
        break

    # If it's a good move, change the player's position
    # If it's a bad move, don't change anything!
    # if the new player position is door, they win!
    # If the new player position is monster, they lose!
    # Otherwise, continue.
