import tkinter as tk
import pygame
import os
from src.tic_tac_toe_logic import TicTacToeLogic

class TicTacToeGUI:
    def __init__(self, root):
        self.game = TicTacToeLogic()
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)

        pygame.mixer.init()

        self.sounds = {
            "click": pygame.mixer.Sound(os.path.join("src", "sounds", "click.wav")),
            "win": pygame.mixer.Sound(os.path.join("src", "sounds", "win.wav")),
            "tie": pygame.mixer.Sound(os.path.join("src", "sounds", "tie.wav"))
        }

        # Track if the game is over
        self.game_over = False

        # Colors
        self.color_blue = "#4584b6"
        self.color_yellow = "#ffde57"
        self.color_gray = "#343434"
        self.color_light_gray = "#646464"

        self.frame = tk.Frame(self.root)
        self.label = tk.Label(self.frame, text=f"{self.game.current_player}'s turn",
                              font=("Consolas", 20), background=self.color_gray, foreground="white")
        self.label.grid(row=0, column=0, columnspan=3, sticky="we")

        self.board_buttons = []
        for row in range(3):
            button_row = []
            for column in range(3):
                button = tk.Button(self.frame, text="", font=("Consolas", 50, "bold"),
                                   background=self.color_gray, foreground=self.color_blue, width=4, height=1,
                                   command=lambda r=row, c=column: self.set_tile(r, c))
                button.grid(row=row + 1, column=column)
                button_row.append(button)
            self.board_buttons.append(button_row)

        self.button = tk.Button(self.frame, text="Restart", font=("Consolas", 20), background=self.color_gray,
                                foreground="white", command=self.new_game)
        self.button.grid(row=4, column=0, columnspan=3, sticky="we")

        self.frame.pack()
        self.center_window()

    def set_tile(self, row, column):
        """Handles the player's move and updates the UI."""
        if self.game_over:  # Ignore clicks if the game is over
            return

        if self.game.board[row][column] == "":  # Play click sound only on valid moves
            self.sounds["click"].play()

        self.game.set_tile(row, column)
        self.update_board()
        winner, winning_positions = self.game.check_winner()

        if winner:
            self.game_over = True  # Set game over flag
            if winner == "Tie":
                self.label.config(text="Tie!", foreground=self.color_yellow)
                self.sounds["tie"].play()  # Play tie sound
            else:
                self.label.config(text=f"{winner} is the winner!", foreground=self.color_yellow)
                self.sounds["win"].play()  # Play win sound
                for r, c in winning_positions:
                    self.board_buttons[r][c].config(foreground=self.color_yellow, background=self.color_light_gray)
        else:
            self.label.config(text=f"{self.game.current_player}'s turn")

    def update_board(self):
        """Updates the board UI with the latest game state."""
        for row in range(3):
            for column in range(3):
                self.board_buttons[row][column].config(text=self.game.board[row][column])

    def new_game(self):
        """Resets the game for a new match."""
        self.game.new_game()
        self.game_over = False  # Reset game over flag
        self.label.config(text=f"{self.game.current_player}'s turn", foreground="white")
        for row in range(3):
            for column in range(3):
                self.board_buttons[row][column].config(text="", foreground=self.color_blue, background=self.color_gray)
        pygame.mixer.stop()  # Stop any ongoing sounds

    def center_window(self):
        """Centers the game window on the screen."""
        self.root.update()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_x = (screen_width - window_width) // 2
        window_y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")