
def possible_win_combinations(board):

    winning_lines =  [
    # rows
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
    # columns
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[3], board[5], board[8]],
    # diagonals
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
        
    ]
    return winning_lines
