import random
from typing import List, NoReturn, Optional, Tuple


class Board:

    def __init__(self):
        """A class to represent the tie tac toe board."""
        self.board: List[List[Optional[str]]] = [[None] * 3 for _ in range(3)]

    def __getitem__(self, index: int) -> Optional[str]:
        """Gives the symbol of a box from the board."""
        row, col = self._get_row_col(index)
        return self.board[row][col]

    def __setitem__(self, index: int, value: str) -> NoReturn:
        """Set the box with payer symbol."""
        row, col = self._get_row_col(index)
        self.board[row][col] = value

    def __repr__(self) -> str:
        """Return a printable representation of the board."""
        return '\n'.join(' '.join(symbol or ' ' for symbol in line) for line in self.board)

    @staticmethod
    def _get_row_col(index: int) -> Tuple[int, int]:
        """Translate index into row and column."""
        return divmod(index - 1, 3)

    @property
    def is_win(self) -> bool:
        """Check if there is a win condition."""
        return self.is_diagonals or self.is_line or self.is_column

    @property
    def is_full(self) -> bool:
        """Check if the board contains any empty boxes."""
        return all(None not in line for line in self.board)

    @property
    def is_line(self) -> bool:
        """Check if the board contains a whole line of same symbol."""
        return any(a == b == c and a is not None for a, b, c in self.board)

    @property
    def is_column(self) -> bool:
        """Checks if the board contains a column of same symbol."""
        return any(a == b == c and a is not None for a, b, c in zip(*self.board))

    @property
    def is_diagonals(self) -> bool:
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

    def choose(self) -> int:
        """Force the player to enter an valid index."""
        choice: str = input("Where do you want to play: ")

        if not choice.isdigit():
            print("Please enter a valid number.")
            return self.choose()

        choice: int = int(choice)
        if choice > 9 or choice < 1:
            print("Please choose an box between 1 and 9.")
            return self.choose()

        return choice


class Game:

    def __init__(self):
        """Core game class."""
        self.board: Board = Board()
        self.players: List[Player, Player] = [Player('x'), Player('o')]

        if random.randint(0, 1):
            self.players: List[Player, Player] = self.players[::-1]

        self.is_running: bool = False

    def handle_player_turn(self, player: Player) -> NoReturn:
        """Player turn behavior."""
        print(f"Player {player.symbol} turns !")
        print(self.board)

        index: int = player.choose()

        while self.board[index] is not None:
            print("Please select a empty box !")
            index: int = player.choose()

        self.board[index]: str = player.symbol

    def handle_game_loop(self) -> NoReturn:
        """Game loop repeated until the game is over."""
        for player in self.players:
            self.handle_player_turn(player)

            if self.board.is_win:
                print(f"{player.symbol} won the game !")
                self.is_running: bool = False
                break

            if self.board.is_full:
                print("It's a tie !")
                self.is_running: bool = False
                break

    def main(self) -> NoReturn:
        """Game entry and main function."""
        self.is_running: bool = True

        while self.is_running:
            self.handle_game_loop()


if __name__ == '__main__':
    game = Game()
    game.main()
