# function for printing board state after each move to mimic a "replay".
import sys
import time

def replay(board_states):
    for board in board_states:
        board.show_board()
        print("\n----------\n")
        time.sleep(2.5)
        sys.stdout.flush()