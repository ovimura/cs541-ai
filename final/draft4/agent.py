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
            print("{} is in white occupied position".format(m))
        if m in self.grid['black']:
            self.status = -1
            print("{} is in black occupied position".format(m))
        if self.get_turn() == 1:
            self.grid["black"].add(m)
            self.board.remove(m)
            self.status = 1
        else:
            self.grid["white"].add(m)
            self.board.remove(m)
            self.status = 1
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
    def evaluate(state, player_color):
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
    def action(s, m):
        new_state = deepcopy(s)
        if "pass" in m:
            return new_state
        new_state.move(m)
        return new_state

    @staticmethod
    def try_move(move, s):
        '''
        It make s copy of the game state.
        :param move: 
        :param s: 
        :return: 
        '''
        m = Move().convert_to_coord(move)
        next_state = HelperMinimax.action(s,move)
        st = s.game_rules.try_move(m)
        s.status = st
        next_state.status = st
        if st == 0:
            next_state.status = 1 # continue the game
        next_state.change_turn()
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
        # print("info : Wait AI is choosing")
        start_time = time.time()
        eval_score, move = self._minimax(0,s,True, self.min, self.max)
        #eval_score, move = self._minimax(0,simulation,True, self.min, self.max)
        stus = HelperMinimax.try_move(move, simulation).status
        print("status (me): {}".format(stus))
        ll =0
        while stus < 0:
            eval_score, move = self._minimax(0,s,True, self.min, self.max)
            #eval_score, move = self._minimax(0,simulation,True, self.min, self.max)
            stus = HelperMinimax.try_move(move, simulation).status
            # print("miss prediction -> status (me): {}; moves left: {}".format(stus, s.moves))
            if len(s.moves) == 0 or ll > 2:
                return 0,'pass'
            ll += 1
        # print("MINIMAX : Done, score = %d, nodes searched %d" % (eval_score, self.node_expanded))
        # print("--- %s seconds ---" % (time.time() - start_time))
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
            return HelperMinimax.evaluate(state, self.player_color), ""

        self.node_expanded += 1
        possible_moves = HelperMinimax.get_possible_moves(state)

        moves = list(possible_moves)
        random.shuffle(moves) #randomness
        best_value = float('-inf') if is_max_turn else float('inf')
        action_target = ""
        for move in moves:
            new_state = HelperMinimax.action(state,move)
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


