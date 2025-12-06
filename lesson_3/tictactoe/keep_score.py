def keep_score(board, player_score, computer_score, GAMES_TO_WIN):
    winner = detect_winner(board)
    
    if winner == 'Player':
        player_score += 1
    elif winner == 'Computer':
        computer_score += 1

    if player_score == GAMES_TO_WIN:
        print(f'PLAYER IS VICTORIOUS, {player_score} to {computer_score}! Well done!')
    elif computer_score == GAMES_TO_WIN:
        print(f'The AIs have won this won, {computer_score} to {player_score}! Better luck next time!')
    elif player_score == computer_score:
        print(f'The game is tied {player_score} to {computer_score}.')
    elif player_score > computer_score:
        print(f'Player is winning {player_score} to {computer_score}!')
    elif computer_score < player_score:
        print(f'Computer is winning {computer_score} to {player_score}!')

    return player_score, computer_score