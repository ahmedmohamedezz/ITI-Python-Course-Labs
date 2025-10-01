from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, symbol) -> None:
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def make_move(self, board) -> None:
        pass


class HumanPlayer(Player):
    def __init__(self, name, symbol) -> None:
        super().__init__(name, symbol)

    def make_move(self, board: "Board") -> None:
        w = board.width
        h = board.height
        while True:
            try:
                x, y = map(int, input(f"enter your move (X Y) (0-{w - 1}): ").split())

                if 0 <= x < w and 0 <= y < h:
                    if board.is_empty_cell(x, y):
                        board.update(x, y, self.symbol)
                        return
                    else:
                        print("Cell is not empty. Try again.")
                else:
                    print(
                        f"Invalid input. Please enter values between 0 and {w - 1} for X and 0 and {h - 1} for Y."
                    )
            except ValueError:
                print("Invalid input. Please enter integer values.")


class ComputerPlayer(Player):
    def __init__(self, name, symbol) -> None:
        super().__init__(name, symbol)

    def make_move(self, board: "Board") -> None:
        w = board.width
        h = board.height
        for x in range(w):
            for y in range(h):
                if board.is_empty_cell(x, y):
                    board.update(x, y, self.symbol)
                    return


class Board:
    def __init__(self) -> None:
        self.__width = 3
        self.__height = 3
        self.__board = [["."] * self.__width for _ in range(self.__height)]
        self.symbols = ["X", "O"]

    def __str__(self) -> str:
        res = ""
        for i in range(self.__height):
            for j in range(self.__width):
                res += f" {self.__board[i][j]} "
            res += "\n"
        return res

    # setters & getters
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, w: int) -> None:
        if w <= 0:
            raise ValueError("board can't have non-positive dimensions")

        self.__width = w

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, h: int) -> None:
        if h <= 0:
            raise ValueError("board can't have non-positive dimensions")

        self.__height = h

    def display(self):
        # use __str__ method
        print(self)

    def update(self, x: int, y: int, symbol: str) -> bool:
        if not self._is_valid_cell(x, y):
            print("Cell is not valid")
            return False

        if not self.is_empty_cell(x, y):
            print("Cell is not empty")
            return False

        if not self._is_valid_symbol(symbol):
            print("Symbol is invalid")
            return False

        self.__board[x][y] = symbol
        return True

    def _is_winner(self, symbol) -> bool:
        # horizontal win
        for i in range(self.__height):
            if self.__board[i] == list(symbol * self.__width):
                return True

        # vertical win
        for j in range(self.__width):
            cur = []
            for i in range(self.__height):
                cur.append(self.__board[i][j])

            if "".join(cur) == symbol * self.__height:
                return True

        # diagonal win
        # main diagonal
        if symbol == self.__board[0][0] and (
            self.__board[0][0] == self.__board[1][1]
            and self.__board[0][0] == self.__board[2][2]
            and self.__board[1][1] == self.__board[2][2]
        ):
            return True

        # cross diagonal
        if symbol == self.__board[0][2] and (
            self.__board[0][2] == self.__board[1][1]
            and self.__board[0][2] == self.__board[2][0]
            and self.__board[1][1] == self.__board[2][0]
        ):
            return True

        return False

    def check_winner(self) -> bool:
        # returns true if either of the players has won
        for symbol in self.symbols:
            if self._is_winner(symbol):
                return True

        return False

    def is_full(self) -> bool:
        # check for any non-empty cell
        for i in range(self.__height):
            cnt = 0
            cnt += self.__board[i].count(".")
            if cnt:
                return False

        return True

    def _is_valid_cell(self, x: int, y: int) -> bool:
        return 0 <= x <= self.__width and 0 <= y <= self.__height

    def is_empty_cell(self, x: int, y: int) -> bool:
        return self.__board[x][y] == "."

    def _is_valid_symbol(self, symbol) -> bool:
        return symbol in self.symbols


class Game:
    def __init__(self, players: list[Player], board: Board, current_turn) -> None:
        self.players = players
        self.board = board
        self.current_turn = current_turn

    def switch_turns(self) -> None:
        # 1 -> player1, 2 -> player2
        self.current_turn = 3 - self.current_turn

    def play(self) -> None:
        player_idx = self.current_turn - 1

        print("----------------------- Current Board State: -----------------------")
        print(f"Player {self.players[player_idx].name}'s turn")
        self.board.display()

        # determine which player will move at this turn
        self.players[player_idx].make_move(self.board)

        if self.board.check_winner():
            print(f"{self.players[player_idx].name} wins!")
            return

        if self.board.is_full():
            print("It's a draw!")
            return

        # switch turns after each play
        self.switch_turns()


if __name__ == "__main__":
    choice = input(
        "Choose (1) to play with friend or (2) to play with computer: "
    ).strip()

    while choice not in ["1", "2"]:
        choice = input(
            "Invalid choice. Choose (1) to play with friend or (2) to play with computer: "
        )

    if choice == "1":
        name1 = input("Enter name for Player 1 (symbol X): ")
        name2 = input("Enter name for Player 2 (symbol O): ")
        player1 = HumanPlayer(name1, "X")
        player2 = HumanPlayer(name2, "O")
    else:
        name1 = input("Enter your name (symbol X): ")
        player1 = HumanPlayer(name1, "X")
        player2 = ComputerPlayer("Computer", "O")

    board = Board()
    game = Game([player1, player2], board, 1)

    while True:
        game.play()
        if game.board.check_winner() or game.board.is_full():
            print("Final Board State:")
            game.board.display()
            break
