from tkinter import Tk
from src.tic_tac_toe_gui import TicTacToeGUI

if __name__ == "__main__":
    root = Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
