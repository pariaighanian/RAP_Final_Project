import copy

class TicTacToeLogic:
    def __init__(self):
        """Initialize the game logic."""
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.turns = 0

    def set_tile(self, row, column):
        """Handles placing a mark and switching players."""
        if self.game_over or self.board[row][column] != "":
            return  # Ignore invalid moves

        self.board[row][column] = self.current_player
        self.turns += 1

        winner, winning_positions = self.check_winner()
        if not winner:
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Checks for a winner or tie and returns the winner with winning positions."""
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                self.game_over = True
                return self.board[row][0], [(row, 0), (row, 1), (row, 2)]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                self.game_over = True
                return self.board[0][col], [(0, col), (1, col), (2, col)]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            self.game_over = True
            return self.board[0][0], [(0, 0), (1, 1), (2, 2)]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.game_over = True
            return self.board[0][2], [(0, 2), (1, 1), (2, 0)]

        # Check for tie
        if self.turns == 9:
            self.game_over = True
            return "Tie", []

        return None, []

    def new_game(self):
        """Resets the board and game state."""
        self.board = copy.deepcopy([[""] * 3 for _ in range(3)])
        self.current_player = "X"
        self.game_over = False
        self.turns = 0
