"""
PROBLEM:
- Check the winning lines to see if player has two in a row

"""

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
               and board[sq2] == HUMAN_MARKER
               and board[sq3] == INITIAL_MARKER):
            board[sq3] = COMPUTER_MARKER

        elif (board[sq2] == COMPUTER_MARKER
                  and board[sq3] == COMPUTER_MARKER
                  and board[sq1] == INITIAL_MARKER):
            board[sq3] = COMPUTER_MARKER
        else:
            square = random.choice(empty_squares(board))
            board[square] = COMPUTER_MARKER