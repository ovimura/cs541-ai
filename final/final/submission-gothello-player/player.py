#!/usr/bin/python3
# CS541: AI
# Student: Ovidiu Mura
# Date: December 10, 2019
# Minimax player implementation


import gthclient
from minimax import *
import sys

if len(sys.argv) != 5:
	print("usage: python3 player.py <color> <host_name> <host_number> <depth>")
	exit(0)

color = sys.argv[1]
host_name = sys.argv[2]
host_number = sys.argv[3]
depth = int(sys.argv[4])

client = gthclient.GthClient(color, host_name, int(host_number))

if 'black' in color:
	ma = Minimax(depth,1)
else:
	ma = Minimax(depth,0)

s = State() # actual game
sim = State() # simulation of actual, checking the rules
i = 1
while True:
	if 'black' in color:
		move = ma.choose_action(s,sim)[1]
		print("{}. me:{}".format(i,move))
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
			print("{}. opp: {}".format(i, move))
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
			print("{}. opp: {}".format(i,move))
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
		print("{}. me:{}".format(i,move))
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
	i += 1
	print()
if int(sim.game_rules.count_score()[0]) > int(sim.game_rules.count_score()[1]):
	print("Black Wins.")
else:
	print("White Wins.")
