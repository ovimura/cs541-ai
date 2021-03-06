#!/usr/bin/python3
# Student: Ovidiu Mura

# minimax move black player
import gthclient
from agent import *
import sys

if len(sys.argv) != 5:
    print("usage: python minimax.py <color> <host_name> <host_number> <depth>")

color = sys.argv[1]
host_name = sys.argv[2]
host_number = sys.argv[3]
depth = int(sys.argv[4])

client = gthclient.GthClient(color, host_name, int(host_number))

if 'black' in color:
	ma = MinimaxAgent(depth,1)
else:
	ma = MinimaxAgent(depth,0)

s = State() # actual game
sim = State() # simulation of actual, checking the rules

while True:
	if 'black' in color:
		move = ma.choose_action(s,sim)[1]
		print("me:", move)
		if move != 'pass':
			try:
				client.make_move(move)
				s.grid["black"].add(move)
				s.board.remove(move)
				s.moves.remove(move)
			except gthclient.MoveError as e:
				if e.cause == e.ILLEGAL:
					print("me: made illegal move, passing")
					client.make_move("pass")
		else:
			print("me: no legal moves left, passing")
			try:
				client.make_move("pass")
			except:
				print("Game Drawn.")
				exit(0)
		sim.game_rules.print_board()
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
		sim.game_rules.print_board()
	else:
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
				s.grid["black"].add(move)
				s.moves.remove(move)
		except gthclient.MoveError as e:
			pass
		sim.game_rules.print_board()
		move = ma.choose_action(s,sim)[1]
		print("me:", move)
		if move != 'pass':
			try:
				client.make_move(move)
				s.grid["white"].add(move)
				s.board.remove(move)
				s.moves.remove(move)
			except gthclient.MoveError as e:
				if e.cause == e.ILLEGAL:
					print("me: made illegal move, passing")
					client.make_move("pass")
		else:
			print("me: no legal moves left, passing")
			client.make_move("pass")
		sim.game_rules.print_board()
