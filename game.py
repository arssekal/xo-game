from menu import Menu
from board import Board
from player import Player
import os
os.system("cls")
class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_index = 0
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == 1:
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    def setup_players(self):
        for i in range (2):
            os.system("cls")
            print(f"player {i+1} enter your details :")
            self.players[i].chose_name()
            self.players[i].choose_symbole()
    def play_game(self):
        while True:
            self.board.display_board()
            if self.play_turn() == 0:
                print(f"it's {self.players[0].name} turn your symbole ({self.players[0].symbole}):")
                choice = int(input("enter a position: "))
                self.board.update_board(choice, self.players[0].symbole)
                self.current_index = 0
            else:
                print(f"it's {self.players[1].name} turn your symbole ({self.players[1].symbole}):")
                choice = int(input("enter a position: "))
                self.board.update_board(choice, self.players[1].symbole)
                self.current_index = 1

    def play_turn(self):
        if self.current_index == 0:
            return 1
        else :
            return 0
    def check_win(self):
        pass
    def check_draw(self):
        for i in self.board.board:
            if i.isalpha():
                k += 1
        return k != 9 
    def restart_game(self):
        self.board.reset_board()
    def quit_game(self):
        print("thank you for playing!")
game = Game()
game.start_game()
game.play_game()