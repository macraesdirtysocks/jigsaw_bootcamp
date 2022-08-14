class Player:
    def __init__(self, name="", shape=""):
        self.name = name
        self.shape = shape
        self.win_pattern = [self.shape, self.shape, self.shape]