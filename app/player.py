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
