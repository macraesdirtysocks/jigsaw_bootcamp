from helper_functions.is_coercible_to_integer import is_coercible_to_integer
def check_move(move, available_board_spaces, current_board_state):
        """
        Check that input is valid.
        1. Input is string, can it be coereced to integer?
        2. Is space on board available?
        3. Is selection in range?
        """
        
        if is_coercible_to_integer(move):
            move_coereced = int(move)
            move_is_available = move_coereced in available_board_spaces
            move_is_in_range = move_coereced in range(0,10)

            if move_is_in_range and move_is_available:
                return move_coereced
            elif not move_is_in_range:
                current_board_state
                print ("Selection out of range, make a selection between 1 and 9.")
                return False
            elif not move_is_available:
                current_board_state
                print("Your selection on the board is already occupied, please make another selection")
                return False
            else:
                current_board_state
                print(f"Move selection {move_coereced} is not available for ugh....reasons...")
                return False
        else:
            print ("Move not an integer")