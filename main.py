from src.player import Player
from src.board import Board
from src.game import Game
from src.move import Move
import sys
import time

# function for printing stdout slowly.
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

# function for printing board state after each move to mimic a "replay".
def replay():
    for state in test_game.in_game_board_state_history:
        state.show_board()
        print("\n----------\n")
        time.sleep(2.5)
        sys.stdout.flush()

# function to capture input for player name and icon selection
def player_create(contestant):
    player_name = input(f"{contestant} enter a name : ")
    player_icon = input(f"{contestant} enter an icon : ")
    return [player_name, player_icon]

"""
* True by default this variable restarts another game.
* After each game the player will be asked if they deire another game.
"""
REMATCH = True

# Inital greeting message printed slowly
intro_message = "Welcome to another tic-tac-toe match!  Let's get to know the players!\n"
print_slow(intro_message)

# Init first player
player_1_info = player_create("Player 1")
player_1 = Player(player_1_info[0], player_1_info[1])

# Init second player
player_2_info = player_create("Player 2")
player_2 = Player(player_2_info[0], player_2_info[1])

# Init the board
board = Board()

# Init a game
test_game = Game(player_1, player_2, board)

# Create message variable from player classes.
game_message_base = f"\nTodays competitors are {test_game.players[0].name} and {test_game.players[1].name}."
game_message_tail = f"The board is ready and {test_game.first_to_play.name} playing {test_game.first_to_play.shape}\'s has first go!"
game_setup_message = f"{game_message_base}\n{game_message_tail}"

# Print init message slowly.
print_slow(game_setup_message)

# Outer while loop runs until no more matches are desired.
while REMATCH is True:
    
    # Inner while loop runs until there are no more empty tile on the board or a player achieves a victory
    while test_game.board.state.count('-') != 0 and test_game.winner is None:
        # Print board before each turn.
        test_game.board.show_board()
        # Make a move for respective player.
        test_game.make_move()
    
    """
    * If while loop is exited and self.winner == None a tie game is declared.
    * Else a wiiner is declare and we do some fancy stuff to celabrate.
    """ 
    if test_game.winner is None:
        print("Tie game!")
    else:
        print("WINNER WINNER CHICKEN DINNER")
        print(f"Congratulations {test_game.winner}")
        # time.sleep(5.0)
        sys.stdout.flush()
    
    # Ask if players would like to see a replay of the macth.
    replay_match = input("Would like to see the match replay? (y/n) :")
    if replay_match == 'y':
        replay()
    
    # Ask if a rematch is desried and update REMATCH variable.
    want_rematch = input("Would like to play again? (y/n) :")
    if want_rematch == "n":
        print("Thanks for playing tic-tac-toe!!!")
        REMATCH = False
            