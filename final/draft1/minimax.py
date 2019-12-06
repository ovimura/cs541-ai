#!/usr/bin/python3
# Student: Ovidiu Mura

# minimax move black player
import gthclient
from agent import *

client = gthclient.GthClient("black", "localhost", 0)

ma = MinimaxAgent(3,1)

s = State() # actual game
sim = State() # simulation of actual, checking the rules

while True:
    s.show_positions()
    #move = AI.get_random_move(s)
    move = ma.choose_action(s,sim)[1]
    print("me:", move)
    if move != 'pass':
        try:
            client.make_move(move)
            s.grid["black"].add(move)
            s.board.remove(move)
            s.moves.remove(move)
        except gthclient.MoveError as e:
            s.add_to_illegal_list(move)
            if e.cause == e.ILLEGAL:
                print("me: made illegal move, passing")
                client.make_move("pass")
    else:
        print("me: no legal moves left, passing")
        client.make_move("pass")

    s.show_positions()
    try:
        cont, move = client.get_move()
        ma.update_rules(sim, move)
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
    except gthclient.MoveError as e:
        pass
