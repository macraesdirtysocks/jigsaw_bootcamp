from src.tic_tac_toe import play_tic_tac_toe
from src.player import Player
from helper_functions.print_slow import print_slow
import sys

REMATCH = True

# function to capture input for player name and icon selection
def player_create(contestant):
    player_name = input(f"{contestant} enter a name : ")
    player_icon = input(f"{contestant} enter an icon : ")
    return [player_name, player_icon]

# Inital greeting message printed slowly
intro_message = "Welcome to another tic-tac-toe match!  Let's get to know the players!\n"
print_slow(intro_message)

# Init first player
player_1_info = player_create("Player 1")
player_1 = Player(player_1_info[0], player_1_info[1])

# Init second player
player_2_info = player_create("Player 2")
player_2 = Player(player_2_info[0], player_2_info[1])

# Create message variable from player classes.
player_intro_message = f"\nTodays competitors are {player_1.name} and {player_2.name}.\n"
print_slow(player_intro_message)

if __name__ == "__main__":

    while REMATCH:
        play_tic_tac_toe(player_1, player_2)

        # Ask if a rematch is desried and update REMATCH variable.
        want_rematch = input("Would like to play again? (y/n) :")
        if want_rematch == "y":
            print("******Resetting board******")
        else:
            print_slow("Thanks for playing tic-tac-toe!!!\n")
            REMATCH = False
