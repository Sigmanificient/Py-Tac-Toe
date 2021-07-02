import random


class Board:

    def __init__(self):
        self.board = [[None, None, None] for _ in range(3)]

    def __getitem__(self, index):
        row, col = self._get_row_col(index)
        return self.board[row][col]

    def __setitem__(self, item, value):
        row, col = self._get_row_col(index)
        self.board[row][col] = value

    def __repr__(self):
        return '\n'.join(' '.join(symbol or ' ' for symbol in line) for line in self.board)

    def is_empty(self, index):
        return self[index] is None

    def set_box(self, index, symbol):
        self[index] = symbol

    @staticmethod
    def _get_row_col(index):
        return divmod(index - 1, 3)

    @property
    def is_win(self):
        """Check if there is a win condition."""
        return self.is_diagonals or self.is_line or self.is_column

    @property
    def is_line(self):
        return any(a == b == c and a is not None for a, b, c in self.board)

    @property
    def is_column(self):
        """For every column of the board, checks if 3 time same symbol."""
        return any(a == b == c and a is not None for a, b, c in zip(*self.board))

    @property
    def is_diagonals(self):
        """Check if one of the two diagonals have the 3 same symbol """
        if self.board[1][1] is None:
            return False

        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True

        return False


class Player:

    def __init__(self, symbol):
        self.symbol = symbol

    def choose(self):
        pass

        # TODO: ask where to play
        # TODO: if choice not valid  (1..9) => retry


class Game:

    def __init__(self):
        self.board = Board()
        self.players = [Player('x'), Player('o')]

        if random.randint(0, 1):
            self.players = self.players[::-1]

        self.is_running = True

    def main(self):
        while self.is_running:

            for player in self.players:
                print(self.board)
                index = player.choose()

                while not self.board.is_empty(index):
                    print("Please select a empty box !")
                    index = player.choose()

                if self.board.is_win():
                    print(f"{player.symbol} won the game !")
                    self.is_running = False
                    break  # exit the for loop


game = Game()
game.main()
