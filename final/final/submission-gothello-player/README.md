Student: Ovidiu Mura
Assignemnt: Gothello
CS541: AI

I implemented a minimax Gothello player. I implemented a depth-limited minimax search. 
I used number of pieces on each side as a heuristic. My implementation minimax player's 
interface can play with the Official Game Server.

I impemented the player in Python programming language. I used minimax algorithm with alpha, beta pruning. 
My implementation abrstration has the following classes:
 - State : this class contains the implementation of the state of a game
 - HelperMinimax : this class contains the implementation of the helper function which is a layer
 between State object and the Minimax instance.
 - Minimax : this class contains the implementation of the Minimax algorithm.
 - Move : this class implements the Move class version from the server side
 - Board : this class implementation is similar to Board class version from the server side
 
My implementation contains three Python scripts files:
 + player.py : this file contains the code which interacts with the Official server and 
 controls the flow of the my player implementation.
 + game_rules.py : this file contains the implementation of the Move and Board classes which are
 Python versino of the Move, and Board classes from the server side.
 + minimax.py : this file contains the implementation of the State, HelperMinimax, and Minimax classes.
 
I used as evaluation function a counter for white stones and a counter for black stones. Minimax algorithm takes 
decisions using evaluation score of each state of the game to take a minimax step. Alpha and beta factors help
to remove parts of the tree states which are not relevant for the current search.

I learn the following:
- how to implement a player to interact with Gothello server
- implement and use minimax algorithm with alpha, beta pruning factors
- implement helper class to comunicate between minimax algorithm and the state of the game

I would like to implement in future an evaluator using neural networks.

How do I reproduce your work (compile, run test)?

To run my player, after you installed the server and Grossthello player, in the directory with my scripts,
run the following command:

python3 player.py <color> <host_name> <host_number> <depth>

For example:

Run the server command: java Gthd 0

Run the Grossthello player command: java Grossthello white localhost 0 3

Run my player impelmentation, use the command: python3 player.py black localhost 0 3

