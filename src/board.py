class Board:
    def __init__(self):
        self.state = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    def show_board(self):
        print("\n")
        print(self.state[0] + "|" + self.state[1] + "|" + self.state[2])
        print(self.state[3] + "|" + self.state[4] + "|" + self.state[5])
        print(self.state[6] + "|" + self.state[7] + "|" + self.state[8])
        print("\n")