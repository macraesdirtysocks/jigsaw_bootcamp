import random
import copy
from src.player import Player
from src.board import Board
from src.move import Move
from helper_functions.check_move import check_move
from helper_functions.is_coercible_to_integer import is_coercible_to_integer 
from helper_functions.build_board_in_game_state import build_board_in_game_state

class Game:
    def __init__(
        self,
        player_1 = Player(),
        player_2 = Player(),
        board = Board()
    ):
        self.players = [player_1, player_2]
        self.board = board
        self.move_history = []
        self.winner = None
        # randomly choose who plays first
        self.first_to_play = random.choice(self.players)
        self.in_game_board_state = self.board.state
        self.in_game_board_state_history = []
        
        # assign who plays first as current player turn
        # this will get updated by a function later on but
        # as a default it is set to self.first_to_play
        self.current_player_turn = self.first_to_play
        
        # create a mapping of player moves that computer can interprete as a list
        # essentially compesate for list indicies starting at 0
        self.available_board_spaces = {v:k for k,v in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9])}
        self.move_history = {}

    # update current player by taking the player from self.players not equal to current player
    def update_current_player(self):
        current_player = self.current_player_turn
        next_turn_player = [player for player in self.players if player != current_player][0]
        self.current_player_turn = next_turn_player

    """
    A win pattern is 3 in a row i.e. ["X", "X", "X"], this is stored on the player class.  The in_game_board_state function 
    builds a list of possible winners and compares them to the current_players win pattern to check if there is a winner.
    """
    def check_winner(self):
        if self.current_player_turn.win_pattern in self.in_game_board_state:
            # This commented out code finds the last move made if move resulted in a win.
            # winning_move_key = [k for k in self.move_history.keys() if k == max(self.move_history.keys())][0]
            # winning_move = self.move_history[winning_move_key]
            self.winner = self.current_player_turn.name

    
    def make_move(self):
            move = input(f"{self.current_player_turn.name}, it's you're turn, make a selection between 1-9: ")
            valid_move = check_move(self, move)
            

            if valid_move:
                # Move instance create with player move.
                player_move = Move(self.current_player_turn, valid_move)
                # Create an id for the play move.
                player_move_key = len(self.move_history) + 1
                # Update the move history dict with player move.
                self.move_history[player_move_key] = player_move
                # Map move to board list, list starts at index 0 so connect input value by using self.available_board_spaces dict.
                move_mapped = self.available_board_spaces[valid_move]
                # place move on the board
                self.board.state[move_mapped] = self.current_player_turn.shape
                # append current_board_state to board_state_history
                self.in_game_board_state_history.append(copy.deepcopy(self.board))
                # update available moves
                if len(self.move_history)>=5:
                    # Build new board state of its current state.
                    self.in_game_board_state = build_board_in_game_state(self)
                    # Check board state for a winner.
                    self.check_winner()
                # If no winner pop off player selection becuase it is no longer available.
                self.available_board_spaces.pop(valid_move)
                # Switch player turn
                self.update_current_player()
                # self.move_history
