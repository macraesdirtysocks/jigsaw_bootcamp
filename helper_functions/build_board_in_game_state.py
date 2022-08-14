"""
I didn't have a good name for this but this function essentially reassembles board.state into a grid.
Then the 8 possible way to win tic-tac-toe are fleshed out and filter for containing the default character (no point testing if dimension contains default character).
""" 
def build_board_in_game_state(self):
    def build_row_states(board):
        row_1 = [board[0], board[1], board[2]]
        row_2 = [board[3], board[4], board[5]]
        row_3 = [board[6], board[7], board[8]]
        # if the dimension contains dashes by default a player cannot acieve a vistory via that dimesion so 
        # it is not inlcuded as a win possibility for win testing.
        return [row for row in [row_1, row_2, row_3] if row.count("-") == 0]
    
    def build_column_states(board):
        column_1 = [board[0], board[3], board[6]]
        column_2 = [board[1], board[4], board[7]]
        column_3 = [board[3], board[5], board[8]]
        # if the dimension contains dashes by default a player cannot acieve a vistory via that dimesion so 
        # it is not inlcuded as a win possibility for win testing.
        return [column for column in [column_1, column_2, column_3] if column.count("-") == 0]
    
    def build_diagonal_states(board):
        diagonal_1 = [board[0], board[4], board[8]]
        diagonal_2 = [board[2], board[4], board[6]]
        # if the dimension contains dashes by default a player cannot acieve a vistory via that dimesion so 
        # it is not inlcuded as a win possibility for win testing.
        return [diagonal for diagonal in [diagonal_1, diagonal_2] if diagonal.count("-") == 0]
    
    possible_win_combinations = []
    # create a list of lists containing dimesion to test for victory.
    [possible_win_combinations.extend(_list) for _list in [build_row_states(self.board.state), build_column_states(self.board.state), build_diagonal_states(self.board.state)]]
    return possible_win_combinations