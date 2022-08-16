from src.player import Player
from src.board import Board

class Game:
    def __init__(
        self,
        player_1 = Player(),
        player_2 = Player(),
        board = Board()
    ):
        self.players = [player_1, player_2]
        self.board = board