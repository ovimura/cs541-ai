from copy import deepcopy
import time
import random

class State(object):
    def __init__(self):
        self.moves = []
        self.turn = 0
        self.board = {letter + digit
             for letter in self.letter_range('a')
             for digit in self.letter_range('1')}
        self.grid = {"white": set(), "black": set()}
        for x in self.board:
            self.moves.append(x)
        print(len(self.moves))

    @staticmethod
    def letter_range(letter):
        for i in range(5):
            yield chr(ord(letter) + i)

    def show_position(self):
        print(self.board)
        for digit in self.letter_range('1'):
            for letter in self.letter_range('a'):
                pos = letter + digit
                if pos in self.grid["white"]:
                    piece = "O"
                elif pos in self.grid["black"]:
                    piece = "*"
                else:
                    piece = "."
                print(piece, end="")
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


class AI:
    @staticmethod
    def get_random_move(s):
        return s.get_random_move()

    @staticmethod
    def get_possible_moves(state):
        """
        Get all possible action in the state
        ...

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
        #return state.total_eval(player_color)
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
        if m in new_state.grid['white']:
            print(m)
            print(" is in white occupied position")
        if AI.get_player(s) == 1:
            new_state.grid["black"].add(m)
        else:
            new_state.grid["white"].add(m)
        new_state.board.remove(m)
        new_state.change_turn()
        new_state.moves.remove(m)
        return new_state


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

        ...

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
        v = []
        for i in range(5):
            v.append([0,0,0,0,0])
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
        s.show_position()
        AI.is_illegal_move(s)

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

    def choose_action(self, s):
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
        list_action = AI.get_possible_moves(s)
        eval_score, move = self._minimax(0,s,True)
        #AI.is_illegal(s, move)
        print("MINIMAX : Done, eval = %d, expanded %d" % (eval_score, self.node_expanded))
        print("--- %s seconds ---" % (time.time() - start_time))
        return eval_score,move

    def _minimax(self, current_depth, state, is_max_turn):
        """
        Minimax Helper
        :param current_depth: the current tree depth in the recursion
        :param state: the current state in the tree node
        :param is_max_turn: bool check the current's node maximizer or not?
        :return:
        """
        if current_depth == self.max_depth or state.is_terminal():
            return AI.evaluation_function(state, self.player_color), ""

        self.node_expanded += 1
        possible_moves = AI.get_possible_moves(state)

        moves = list(possible_moves)
        random.shuffle(moves) #randomness
        best_value = float('-inf') if is_max_turn else float('inf')
        action_target = ""
        for move in moves:
            new_state = AI.result_function(state,move)
            #print(new_state.moves)
            eval_child, action_child = self._minimax(current_depth+1,new_state,not is_max_turn)

            if is_max_turn and best_value < eval_child:
                best_value = eval_child
                action_target = move

            elif (not is_max_turn) and best_value > eval_child:
                best_value = eval_child
                action_target = move

        return best_value, action_target


# ma = MinimaxAgent(3,1)
#
# print(ma.choose_action(State()))
