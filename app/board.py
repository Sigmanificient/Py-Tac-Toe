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
