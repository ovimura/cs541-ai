#!/usr/bin/python3

# minimax move black player
import gthclient
from agent import *

client = gthclient.GthClient("black", "localhost", 0)

ma = MinimaxAgent(3,1)

s = State()

while True:
    s.show_position()
    #move = AI.get_random_move(s)
    move = ma.choose_action(s)[1]
    print("me:", move)
    try:
        client.make_move(move)
        s.grid["black"].add(move)
        s.board.remove(move)
        s.moves.remove(move)
    except gthclient.MoveError as e:
        if e.cause == e.ILLEGAL:
            print("me: made illegal move, passing")
            client.make_move("pass")

    s.show_position()
    cont, move = client.get_move()
    print("opp:", move)
    if cont and move == "pass":
        print("me: pass to end game")
        client.make_move("pass")
        break
    else:
        if not cont:
            break
        s.board.remove(move)
        s.grid["white"].add(move)
        s.moves.remove(move)
