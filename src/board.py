import copy

class Board:
    def __init__(self):
        self.state = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        self.history = []

    def show_board(self):
        print("\n")
        print(self.state[0] + "|" + self.state[1] + "|" + self.state[2])
        print(self.state[3] + "|" + self.state[4] + "|" + self.state[5])
        print(self.state[6] + "|" + self.state[7] + "|" + self.state[8])
        print("\n")
    
    def available_board_positions(self):
       return [k for k,v in zip(range(1, 10), self.state) if v == "-"]

    def update_history(self):
        self.history.append(copy.deepcopy(self))