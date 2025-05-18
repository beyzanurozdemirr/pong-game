import tkinter as tk
from tkinter import messagebox
import random
from game_logic import create_empty_board, place_ships_randomly, is_game_over

class BattleshipGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Amiral Battı")
        self.board_size = 8
        self.buttons_player = []
        self.buttons_computer = []
        self.player_board = create_empty_board()
        self.computer_board = create_empty_board()
        self.revealed_computer = [[False]*self.board_size for _ in range(self.board_size)]
        self.player_hits = 0
        self.computer_hits = 0
        place_ships_randomly(self.player_board)
        place_ships_randomly(self.computer_board)
        self.create_widgets()

    def create_widgets(self):
        frame_player = tk.Frame(self.root)
        frame_computer = tk.Frame(self.root)
        frame_player.grid(row=0, column=0, padx=10)
        frame_computer.grid(row=0, column=1, padx=10)

        tk.Label(frame_player, text="Senin Tahtan").grid(row=0, column=0, columnspan=self.board_size)
        tk.Label(frame_computer, text="Bilgisayarın Tahtası").grid(row=0, column=0, columnspan=self.board_size)

        for r in range(self.board_size):
            row_buttons = []
            for c in range(self.board_size):
                btn = tk.Button(frame_player, width=2, height=1, text='~', state='disabled')
                btn.grid(row=r+1, column=c)
                row_buttons.append(btn)
            self.buttons_player.append(row_buttons)

        for r in range(self.board_size):
            row_buttons = []
            for c in range(self.board_size):
                btn = tk.Button(frame_computer, width=2, height=1, command=lambda r=r, c=c: self.player_turn(r, c))
                btn.grid(row=r+1, column=c)
                row_buttons.append(btn)
            self.buttons_computer.append(row_buttons)

        self.update_player_board()

    def update_player_board(self):
        for r in range(self.board_size):
            for c in range(self.board_size):
                if self.player_board[r][c] == 'S':
                    self.buttons_player[r][c]['text'] = 'S'
                elif self.player_board[r][c] == 'X':
                    self.buttons_player[r][c]['text'] = 'X'
                elif self.player_board[r][c] == 'O':
                    self.buttons_player[r][c]['text'] = 'O'

    def player_turn(self, r, c):
        if self.revealed_computer[r][c]:
            return  
        self.revealed_computer[r][c] = True

        if self.computer_board[r][c] == 'S':
            self.computer_board[r][c] = 'X'
            self.buttons_computer[r][c]['text'] = 'X'
            self.buttons_computer[r][c]['bg'] = 'red'
            self.player_hits += 1
        else:
            self.computer_board[r][c] = 'O'
            self.buttons_computer[r][c]['text'] = 'O'
            self.buttons_computer[r][c]['bg'] = 'blue'
            self.root.after(500, self.computer_turn)

        if is_game_over(self.computer_board):
            messagebox.showinfo("Tebrikler!", "Tüm gemileri batırdınız! Oyunu kazandınız.")
            self.disable_all_buttons()

    def computer_turn(self):
        while True:
            r = random.randint(0, self.board_size - 1)
            c = random.randint(0, self.board_size - 1)
            if self.player_board[r][c] not in ['X', 'O']:
                break

        if self.player_board[r][c] == 'S':
            self.player_board[r][c] = 'X'
            self.buttons_player[r][c]['bg'] = 'red'
        else:
            self.player_board[r][c] = 'O'
            self.buttons_player[r][c]['bg'] = 'blue'

        self.update_player_board()

        if is_game_over(self.player_board):
            messagebox.showinfo("Kaybettiniz", "Bilgisayar tüm gemilerinizi batırdı.")
            self.disable_all_buttons()

    def disable_all_buttons(self):
        for row in self.buttons_computer:
            for btn in row:
                btn.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    game = BattleshipGame(root)
    root.mainloop()
