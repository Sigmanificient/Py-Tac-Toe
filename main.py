import random


class Board:

    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def is_empty(self, index):
        return

        # TODO: return whether to box at index is empty or not

    def set_box(self, index, symbol):
        pass

        # TODO: set box oof index to correct symbol

    def is_win(self):
        """Check if there is a win condition."""
        return self.is_line() or self.is_column()

    def is_line(self):
        pass
        # TODO: for each line of the board, check if 3 time same symbol

    def is_column(self):
        """For every column of the board, checks if 3 time same symbol."""
        return any(a == b == c and a is not None for a, b, c in zip(*self.board))


class Player:

    def __init__(self, symbol):
        self.symbol = symbol

    def choose(self):
        pass

        # TODO: ask where to play
        # TODO: return the choice


class Game:

    def __init__(self):
        self.board = Board()
        self.players = [...]  # TODO: set 2 players with an unique symbols

        if random.randint(0, 1):
            # Reversing players list to change who plays first
            self.players = self.players[::-1]

        self.is_running = True

    def main(self):
        while self.is_running:

            for player in self.players:
                _ = player.choose()

                # TODO: While index is not valid, ask again
                # TODO: set board index.

                if self.board.is_win():
                    print(f"{player.symbol} won the game !")
                    self.is_running = False
                    break  # exit the for loop


game = Game()
game.main()
