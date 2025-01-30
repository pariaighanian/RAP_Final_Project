import unittest
from src.tic_tac_toe_logic import TicTacToeLogic

class TestTicTacToeLogic(unittest.TestCase):
    
    def setUp(self):
        """Initialize a new game before each test."""
        self.game = TicTacToeLogic()

    def test_initial_state(self):
        """Test the initial state of the game."""
        self.assertEqual(self.game.current_player, "X")
        self.assertFalse(self.game.game_over)
        self.assertEqual(self.game.turns, 0)
        self.assertEqual(self.game.board, [["", "", ""], ["", "", ""], ["", "", ""]])

    def test_set_tile(self):
        """Test setting a tile and switching players."""
        self.game.set_tile(0, 0)
        self.assertEqual(self.game.board[0][0], "X")
        self.assertEqual(self.game.current_player, "O")
        self.assertEqual(self.game.turns, 1)

    def test_prevent_overwriting_tiles(self):
        """Ensure a tile cannot be overwritten after being placed."""
        self.game.set_tile(0, 0)
        self.game.set_tile(0, 0)  # Try overwriting the same spot
        self.assertEqual(self.game.board[0][0], "X")  # Should still be X
        self.assertEqual(self.game.current_player, "O")  # Should not change back to X
        self.assertEqual(self.game.turns, 1)  # Turns should not increase

    def test_check_winner_horizontal(self):
        """Test horizontal win condition."""
        self.game.board = [["X", "X", "X"], ["", "", ""], ["", "", ""]]
        winner, positions = self.game.check_winner()
        self.assertEqual(winner, "X")
        self.assertEqual(positions, [(0, 0), (0, 1), (0, 2)])
        self.assertTrue(self.game.game_over)

    def test_check_winner_vertical(self):
        """Test vertical win condition."""
        self.game.board = [["O", "", ""], ["O", "", ""], ["O", "", ""]]
        winner, positions = self.game.check_winner()
        self.assertEqual(winner, "O")
        self.assertEqual(positions, [(0, 0), (1, 0), (2, 0)])
        self.assertTrue(self.game.game_over)

    def test_check_winner_diagonal(self):
        """Test diagonal win condition."""
        self.game.board = [["X", "", ""], ["", "X", ""], ["", "", "X"]]
        winner, positions = self.game.check_winner()
        self.assertEqual(winner, "X")
        self.assertEqual(positions, [(0, 0), (1, 1), (2, 2)])
        self.assertTrue(self.game.game_over)

    def test_check_winner_anti_diagonal(self):
        """Test anti-diagonal win condition."""
        self.game.board = [["", "", "O"], ["", "O", ""], ["O", "", ""]]
        winner, positions = self.game.check_winner()
        self.assertEqual(winner, "O")
        self.assertEqual(positions, [(0, 2), (1, 1), (2, 0)])
        self.assertTrue(self.game.game_over)

    def test_check_winner_tie(self):
        """Test tie condition."""
        self.game.board = [["X", "O", "X"], ["X", "X", "O"], ["O", "X", "O"]]
        self.game.turns = 9
        winner, positions = self.game.check_winner()
        self.assertEqual(winner, "Tie")
        self.assertEqual(positions, [])  # No winning positions
        self.assertTrue(self.game.game_over)

    def test_no_moves_after_game_over(self):
        """Ensure no moves can be made after the game is over."""
        self.game.board = [["X", "X", "X"], ["", "", ""], ["", "", ""]]
        self.game.game_over = True
        self.game.set_tile(1, 1)
        self.assertEqual(self.game.board[1][1], "")  # Tile should remain empty

    def test_check_winner_does_not_change_state_if_no_winner(self):
        """Ensure check_winner() does not falsely declare a winner."""
        self.game.board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", ""]]
        winner, positions = self.game.check_winner()
        self.assertIsNone(winner)  # There should be no winner
        self.assertFalse(self.game.game_over)  # Game should still be running

    def test_switching_players_correctly(self):
        """Ensure players switch correctly after each move."""
        self.assertEqual(self.game.current_player, "X")
        self.game.set_tile(0, 0)
        self.assertEqual(self.game.current_player, "O")
        self.game.set_tile(0, 1)
        self.assertEqual(self.game.current_player, "X")

    def test_new_game(self):
        """Ensure new_game() resets all values correctly."""
        self.game.board = [["X", "O", "X"], ["X", "X", "O"], ["O", "X", "O"]]
        self.game.current_player = "O"
        self.game.game_over = True
        self.game.turns = 9

        self.game.new_game()

        self.assertEqual(self.game.board, [["", "", ""], ["", "", ""], ["", "", ""]])
        self.assertEqual(self.game.current_player, "X")
        self.assertFalse(self.game.game_over)
        self.assertEqual(self.game.turns, 0)

    def test_player_always_starts_as_X(self):
        """Ensure the first move is always by player X after resetting."""
        self.game.new_game()
        self.assertEqual(self.game.current_player, "X")

