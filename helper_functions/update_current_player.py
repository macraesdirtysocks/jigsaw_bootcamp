# update current player by taking the player from self.players not equal to current player
def update_current_player(current_player, players):
    next_turn_player = [player for player in players if player != current_player][0]
    return next_turn_player