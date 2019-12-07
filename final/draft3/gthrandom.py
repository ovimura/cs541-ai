#!/usr/bin/python3

# Random-move Gothello player.

import random
import sys

import gthclient

me = sys.argv[1]
opp = gthclient.opponent(me)

client = gthclient.GthClient(me, "localhost", 0)

def letter_range(letter):
    for i in range(5):
        yield chr(ord(letter) + i)

board = {letter + digit
         for letter in letter_range('a')
         for digit in letter_range('1')}

grid = {"white": set(), "black": set()}

def show_position():
    for digit in letter_range('1'):
        for letter in letter_range('a'):
            pos = letter + digit
            if pos in grid["white"]:
                piece = "O"
            elif pos in grid["black"]:
                piece = "*"
            else:
                piece = "."
            print(piece, end="")
        print()

side = "black"

while True:
    show_position()
    if side == me:
        move = random.choice(list(board))
        print("me:", move)
        try:
            client.make_move(move)
            grid[me].add(move)
            board.remove(move)
        except gthclient.MoveError as e:
            if e.cause == e.ILLEGAL:
                print("me: made illegal move, passing")
                client.make_move("pass")
    else:
        cont, move = client.get_move()
        print("opp:", move)
        if cont and move == "pass":
            print("me: pass to end game")
            client.make_move("pass")
            break
        else:
            if not cont:
                break
            board.remove(move)
            grid[opp].add(move)

    side = gthclient.opponent(side)
