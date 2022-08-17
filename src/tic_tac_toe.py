import random
from src.board import Board
from src.game import Game
from src.move import Move
from helper_functions.check_move import check_move
from helper_functions.update_current_player import update_current_player
from helper_functions.possible_win_combos import possible_win_combinations
from helper_functions.replay import replay
from helper_functions.print_slow import print_slow
import sys

def play_tic_tac_toe(player_1, player_2):

    # Init the board
    board = Board() 

    # Init a game
    tic_tac_toe = Game(player_1, player_2, board)

    CURRENT_PLAYER_TURN = random.choice(tic_tac_toe.players) # randomly choose who plays first.
    WINNER = None # Set winner variable to None for new game.
    BOARD_MAP = {v:k for k,v in enumerate(range(1, 10))} # List to board map.

    first_play_message = f"The board is ready and {CURRENT_PLAYER_TURN.name} playing {CURRENT_PLAYER_TURN.shape}\'s has first go!\n"
    print_slow(first_play_message)
    
    # Show the board before the first turn.
    tic_tac_toe.board.show_board()
        
    # While loop runs until there are no more empty tile on the board or a player achieves a victory
    while tic_tac_toe.board.state.count('-') != 0 and WINNER is None:

        # Get available board spaces from the board class.
        available_board_spaces = tic_tac_toe.board.available_board_positions()

        current_board_state = tic_tac_toe.board.state

        # Make a move for respective player.
        move = input(f"{CURRENT_PLAYER_TURN.name}, it's you're turn, make a selection between 1-9: ")
        validate_move = check_move(move, available_board_spaces, current_board_state)

        if validate_move:
            # Move instance create with player move.
            player_move = Move(CURRENT_PLAYER_TURN, validate_move)
            # Map move to board list, list starts at index 0 so connect input value by using self.available_board_spaces dict.
            move_mapped = BOARD_MAP[validate_move]
            # place move on the board
            tic_tac_toe.board.state[move_mapped] = CURRENT_PLAYER_TURN.shape
            # Append deep copy of current board to board history.
            tic_tac_toe.board.update_history()
            # Show the board.
            tic_tac_toe.board.show_board()
            # If the number of moves made (length of the history) is greater than 5 test for winner.
            # Winner cannnot exist until move 5.
            if len(tic_tac_toe.board.history)>=5:
                # Check board state for a winner.
                if CURRENT_PLAYER_TURN.win_pattern in possible_win_combinations(tic_tac_toe.board.state):
                    WINNER = True
            
            if WINNER is None:
                CURRENT_PLAYER_TURN = update_current_player(CURRENT_PLAYER_TURN, tic_tac_toe.players)

    """
    * If while loop is exited and self.winner == None a tie game is declared.
    * Else a winner is declare and we do some fancy stuff to celabrate.
    """ 
    if WINNER is None:
        print("Tie game!")
    else:
        print_slow("WINNER WINNER CHICKEN DINNER\n")
        print_slow(f"Congratulations {CURRENT_PLAYER_TURN.name}\n")
        # time.sleep(5.0)
        sys.stdout.flush()
    
    # Ask if players would like to see a replay of the match.
    replay_match = input("Would like to see the match replay? (y/n) :")
    if replay_match == 'y':
        replay(tic_tac_toe.board.history)
    
    