import random


class Board:

    def __init__(self):
        """A class to represent the tie tac toe board."""
        self.board = [[None] * 3 for _ in range(3)]

    def __getitem__(self, index):
        """Gives the symbol of a box from the board."""
        row, col = self._get_row_col(index)
        return self.board[row][col]

    def __setitem__(self, index, value):
        """Set the box with payer symbol."""
        row, col = self._get_row_col(index)
        self.board[row][col] = value

    def __repr__(self):
        """Return a printable representation of the board."""
        return '\n'.join(' '.join(symbol or ' ' for symbol in line) for line in self.board)

    @staticmethod
    def _get_row_col(index):
        """Translate index into row and column."""
        return divmod(index - 1, 3)

    @property
    def is_win(self):
        """Check if there is a win condition."""
        return self.is_diagonals or self.is_line or self.is_column

    @property
    def is_full(self):
        """Check if the board contains any empty boxes."""
        return all(None not in line for line in self.board)

    @property
    def is_line(self):
        """Check if the board contains a whole line of same symbol."""
        return any(a == b == c and a is not None for a, b, c in self.board)

    @property
    def is_column(self):
        """checks if the board contains a column of same symbol."""
        return any(a == b == c and a is not None for a, b, c in zip(*self.board))

    @property
    def is_diagonals(self):
        """Check if one of the two diagonals have the same symbol."""
        if self.board[1][1] is None:
            return False

        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True

        return False


class Player:

    def __init__(self, symbol):
        """A class that keep the symbol of the player and validate user input."""
        self.symbol = symbol

    def choose(self):
        """Force the player to enter an valid index."""
        choice = input("Where do you want to play: ")

        if not choice.isdigit():
            print(f"Please enter a valid number.")
            return self.choose()

        choice = int(choice)
        if choice > 9 or choice < 1:
            print("Please choose an box between 1 and 9.")
            return self.choose()

        return choice


class Game:

    def __init__(self):
        """Core game class."""
        self.board = Board()
        self.players = [Player('x'), Player('o')]

        if random.randint(0, 1):
            self.players = self.players[::-1]

        self.is_running = False

    def handle_player_turn(self, player):
        """Player turn behavior."""
        print(f"Player {player.symbol} turns !")
        print(self.board)

        index = player.choose()

        while self.board[index] is not None:
            print("Please select a empty box !")
            index = player.choose()

        self.board[index] = player.symbol

    def handle_game_loop(self):
        """Game loop repeated until the game is over."""
        for player in self.players:
            self.handle_player_turn(player)

            if self.board.is_win:
                print(f"{player.symbol} won the game !")
                self.is_running = False
                break

            if self.board.is_full:
                print("It's a tie !")
                self.is_running = False
                break

    def main(self):
        """Game entry and main function"""
        self.is_running = True

        while self.is_running:
            self.handle_game_loop()


if __name__ == '__main__':
    game = Game()
    game.main()

