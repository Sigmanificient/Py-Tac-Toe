import random
from typing import List, NoReturn
from app.board import Board
from app.player import Player


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
