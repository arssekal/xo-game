from menu import Menu
from board import Board
from player import Player
import os
def clear():
 os.system("cls")
class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_index = 0
        self.win = []
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == 1:
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    def setup_players(self):
        for i in range (2):
            clear()
            print(f"player {i+1} enter your details :")
            self.players[i].chose_name()
            self.players[i].choose_symbole()
    def play_game(self):
        while self.no_draw() and self.check_win() == False:
            self.board.display_board()
            if self.play_turn() == 0:
                print(f"it's {self.players[0].name} turn your symbole ({self.players[0].symbole}):")
                choice = int(input("enter a position: "))
                while self.board.update_board(choice, self.players[0].symbole) == False:
                    choice = int(input("enter a valid position: "))
                self.current_index = 0
            else:
                print(f"it's {self.players[1].name} turn your symbole ({self.players[1].symbole}):")
                choice = int(input("enter a position: "))
                while self.board.update_board(choice, self.players[1].symbole) == False:
                    choice = int(input("enter a valid position: "))
                self.current_index = 1
        if self.no_draw() == False:
            self.board.display_board()
            print("draw no one win!")
            if self.menu.display_endGame_menu() == 1:
                clear()
                self.board.reset_board()
                self.start_game()
            else :
                self.quit_game()
        if self.check_win():
            # self.board.gain_board(self.win)
            self.board.display_board()
            if self.players[0].symbole == self.board.board[self.win[0]]:
                print(f"{self.players[0].name} win")
            else :
                print(f"{self.players[1].name} win")

            if self.menu.display_endGame_menu() == 1:
                clear()
                self.board.reset_board()
                self.start_game()
            else :
                self.quit_game()

    def play_turn(self):
        if self.current_index == 0:
            return 1
        else :
            return 0
    def check_win(self):
        possible_win = [ [0,1,2],[0,3,6], [0,4,8], [2,5,8],[6,7,8],[3,4,5],[2,4,6],[1,4,7] ]
        saves_k = []
        saves_p = []
        for row in possible_win:
            k = 0
            p = 0
            for i in row:
                if self.board.board[i] == self.players[0].symbole:
                    k += 1
                elif self.board.board[i] == self.players[1].symbole:
                    p += 1
            saves_k.append(k)
            saves_p.append(p)
        if 3 in saves_k:
            self.win = possible_win[saves_k.index(3)]
            return True
        elif 3 in saves_p:
            self.win = possible_win[saves_p.index(3)]
            return True
        else:
            return False

    def no_draw(self):
        k = 0
        for i in self.board.board:
            if i == self.players[0].symbole or i == self.players[1].symbole:
                k += 1
        return k != 9 
    def restart_game(self):
        self.board.reset_board()
    def quit_game(self):
        print("thank you for playing!")
clear()
game = Game()
game.start_game()