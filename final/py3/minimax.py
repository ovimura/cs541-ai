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

    def choose_action(self, state):
        """
        Predict the move using minimax algorithm
        Parameters
        ----------
        state : State
        Returns
        -------
        float, str:
            The evaluation or utility and the action key name
        """
        list_action = AIElements.get_possible_action(state)
        eval_score, selected_key_action = self._minimax(0,state,True)
        return (selected_key_action,list_action[selected_key_action])

    def _minimax(self, current_depth, state, is_max_turn):

        if current_depth == self.max_depth or state.is_terminal():
            return AIElements.evaluation_function(state, self.player_color), ""

        possible_action = AIElements.get_possible_action(state)
        key_of_actions = list(possible_action.keys())

        shuffle(key_of_actions) #randomness
        best_value = float('-inf') if is_max_turn else float('inf')
        action_target = ""
        for action_key in key_of_actions:
            new_state = AIElements.result_function(state,possible_action[action_key])

            eval_child, action_child = self._minimax(current_depth+1,new_state,not is_max_turn)

            if is_max_turn and best_value < eval_child:
                best_value = eval_child
                action_target = action_key

            elif (not is_max_turn) and best_value > eval_child:
                best_value = eval_child
                action_target = action_key

        return best_value, action_target
