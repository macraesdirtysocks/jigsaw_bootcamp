from src.player import Player

class Move:
    def __init__(self, player: Player, player_move):
        self.player = player
        self.move = player_move

    def show_move_history(self):
        return self.move_history