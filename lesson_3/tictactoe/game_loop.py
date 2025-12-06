"""
There are two new functions there: choose_square and alternate_player. 
choose_square is a generic function that knows how to choose a square 
depending on the current player. That is, it will call computer_chooses_square 
or player_chooses_square depending on the value of current_player. The trick, then,
is to keep track of the current player and pass it to choose_square during each turn.

ALGORITHM:
- 

"""

def alternate_player(current_player):
    return 'computer' if current_player == 'player' else 'computer'

def choose_square(board, current_player):
    if current_player == 'player':
        player_chooses_square(board)
    elif current_player == 'computer':
        computer_chooses_square(board)

while True:
    display_board(board)
    choose_square(board, current_player)
    current_player = alternate_player(current_player)
    if someone_won(board) or board_full(board):
        break



