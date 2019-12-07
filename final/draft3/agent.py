from copy import deepcopy
import time
import random
from game_rules import *

class State(object):
    def __init__(self):
        self.last_move = None
        self.status = 0
        self.moves = []
        self.turn = 0
        self.board = {letter + digit
             for letter in self.letter_range('a')
             for digit in self.letter_range('1')}
        self.grid = {"white": set(), "black": set()}
        for x in self.board:
            self.moves.append(x)
        self.illegal_moves = []
        self.game_rules = Board()

    @staticmethod
    def letter_range(letter):
        for i in range(5):
            yield chr(ord(letter) + i)

    def show_positions(self):
        #print(self.board)
        tbl = []
        for digit in self.letter_range('1'):
            tmp = []
            for letter in self.letter_range('a'):
                pos = letter + digit
                if pos in self.grid["white"]:
                    piece = "O"
                elif pos in self.grid["black"]:
                    piece = "*"
                else:
                    piece = "."
                tmp.append(piece)
#                print(piece, end="")
            tbl.append(tmp)
        for i in [4,3,2,1,0]:
            for j in range(5):
                print(tbl[i][j], end="")
            print()

    def get_random_move(self):
        return random.choice(list(self.board))

    def get_possible_moves(self):
        return self.moves

    def is_terminal(self):
        if len(self.moves) == 0:
            return True
        return False

    def change_turn(self):
        self.turn += 1

    def liberties(self):
        return 0

    def get_black_count(self):
        return len(self.grid['black'])

    def get_white_count(self):
        return len(self.grid['white'])

    def get_score(self,color):
        if color == 'black':
            return self.get_black_count()
        else:
            return self.get_white_count()

    def get_turn(self):
        return self.turn % 2

    def add_to_illegal_list(self, m):
        self.illegal_moves.append(m)

    def isValid(self):
        if self.status > 0:
            return True
        else:
            return False

    def isPass(self, m):
        if m in self.grid["white"] or m in self.grid["black"]:
            return True
        elif m in self.moves:
            return False

    def move(self,m):
        self.last_move = m
        if m in self.grid['white']:
            self.status = -1
            print(m)
            print(" is in white occupied position")
        if self.get_turn() == 1:
            self.grid["black"].add(m)
        else:
            self.grid["white"].add(m)
        self.board.remove(m)
        self.change_turn()
        self.moves.remove(m)


class HelperMinimax:
    @staticmethod
    def get_random_move(s):
        return s.get_random_move()

    @staticmethod
    def get_possible_moves(state):
        """
        Get all possible action in the state
        Attributes
        ----------
        state : State
            A state that want to be searched about the possible action.
        Returns
        -------
        dict
            a concatenated all list of actions.
        """
        collected_moves = state.get_possible_moves()
        all_possible_moves = collected_moves #AI._one_move(collected_moves)
        if len(all_possible_moves) == 0:
            return 0
        return all_possible_moves

    @staticmethod
    def evaluation_function(state, player_color):
        return state.get_score(player_color)

    @staticmethod
    def get_player(state):
        """
        Attributes
        ----------
        state : State
            a state S.
            :return 1 : black, 0: white
        """
        return state.get_turn()

    @staticmethod
    def result_function(s, m):
        new_state = deepcopy(s)
        if "pass" in m:
            return new_state
        new_state.move(m)
        return new_state

    @staticmethod
    def get_illegal_moves(s):
        return s.illegal_moves

    def experimental_reward_function(self, old_state, new_state, player_color):
        '''
        Experimental Reward Function
        ----------
        old_state: State
            the state
        new_state: State
            next state
        player_color: int
            player_color
        '''
        return new_state.get_score(player_color) - old_state.get_score(player_color)

    def is_over(self, state):
        """
        Terminal State.

        Attributes
        ----------
        state : State
            a state S.

        Returns
        -------
        end : bool
            Return true if the game has ended in the current state.
        """
        return state.is_terminal()

    @staticmethod
    def is_illegal_move(s):
        v = [[0]*5 for x in range(5)]
        print(v)
        exit(3)
        # for i in range(5):
        #     v.append([0,0,0,0,0])
        for m in s.moves:
            v[ord(m[:-1])-97][int(m[-1])-1] = 1
        for i in range(5):
            for j in range(5):
                if i == 0:
                    if i > 0 and v[i][j] == 0 and v[i-1][j] == 1 and v[i+1][j] == 1 and v[i][j+1] == 1:
                        print(chr(97+i))
        return False

    @staticmethod
    def is_illegal(s,m):
        s.show_positions()
        HelperMinimax.is_illegal_move(s)

    @staticmethod
    def try_move(move, s):
        '''
        It make s copy of the game state.
        :param move: 
        :param s: 
        :return: 
        '''
        m = Move().convert_to_coord(move)
        next_state = HelperMinimax.result_function(s,move)
        st = s.game_rules.try_move(m)
        s.status = st
        next_state.status = st
        # if next_state.isValid() != True:
        #     return -1 # illegal move
        # if next_state.isValid() != True:
        #     return -1 # illegal move
        # if next_state.isPass(move) and s.isPass(move):
        #     next_state.status = -3 # Game Over!!
        #     return next_state
        # if not next_state.move_ok(move):
        #     return -1
        if st == 0:
#            next_state.move(move)
#            next_state.change_turn()
            next_state.status = 1 # continue the game
        return next_state

class MinimaxAgent:
    """
        Minimax agent
    """
    def __init__(self, max_depth, player_color):
        """
        Initiation

        Parameters
        ----------
        max_depth : int
            The max depth of the tree

        player_color : int
            The player's index as MAX in minimax algorithm
        """
        self.max_depth = max_depth
        self.player_color = player_color
        self.node_expanded = 0
        self.min = 0
        self.max = 25


    def choose_action(self, s, simulation):
        """
        Predict the move using minimax algorithm

        Parameters
        ----------
        s : State

        Returns
        -------
        float, str:
            The evaluation or utility and the action key name
        """
        self.node_expanded = 0
        print("MINIMAX : Wait AI is choosing")
        start_time = time.time()
        list_action = HelperMinimax.get_possible_moves(s)
        #print(list_action)
        eval_score, move = self._minimax(0,s,True, self.min, self.max)
        #while HelperMinimax.try_move(move, s) != True:
        stus = HelperMinimax.try_move(move, simulation).status
        print("status (me): {}".format(stus))
        #while move in HelperMinimax.get_illegal_moves(s):
        ll =0
        while stus < 0:
            eval_score, move = self._minimax(0,s,True, self.min, self.max)
            stus = HelperMinimax.try_move(move, simulation).status
            print("loop -> status (me): {}; moves left: {}".format(stus, s.moves))
            #if HelperMinimax.get_illegal_moves(s).sort() == HelperMinimax.get_possible_moves(s).sort():
            #    return 0,'pass'
            if len(s.moves) == 0 or ll > 5:
                return 0,'pass'
            ll += 1
        #AI.is_illegal(s, move)
        print("MINIMAX : Done, eval = %d, expanded %d" % (eval_score, self.node_expanded))
        print("--- %s seconds ---" % (time.time() - start_time))
        return eval_score,move

    def _minimax(self, current_depth, state, is_max_turn, alpha, beta):
        """
        Minimax Helper
        :param current_depth: the current tree depth in the recursion
        :param state: the current state in the tree node
        :param is_max_turn: bool check the current's node maximizer or not?
        :return:
        """
        if current_depth == self.max_depth or state.is_terminal():
            return HelperMinimax.evaluation_function(state, self.player_color), ""

        self.node_expanded += 1
        possible_moves = HelperMinimax.get_possible_moves(state)

        moves = list(possible_moves)
        random.shuffle(moves) #randomness
        best_value = float('-inf') if is_max_turn else float('inf')
        action_target = ""
        for move in moves:
            new_state = HelperMinimax.result_function(state,move)
            #print(new_state.moves)
            eval_child, action_child = self._minimax(current_depth+1,new_state,not is_max_turn, alpha, beta)

            if is_max_turn and best_value < eval_child:
                best_value = eval_child
                alpha = max(alpha, best_value)
                action_target = move
                if beta <= alpha:
                    break
            elif (not is_max_turn) and best_value > eval_child:
                best_value = eval_child
                beta = min(beta, best_value)
                action_target = move
                if beta <= alpha:
                    break
        return best_value, action_target

    def update_rules(self, sim, move):
        print("status (opp): {}".format(HelperMinimax.try_move(move, sim).status))


# ma = MinimaxAgent(7,1)
# print(ma.choose_action(State(), State()))
