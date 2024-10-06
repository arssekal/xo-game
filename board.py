class Board:
    def __init__(self):
        self.board = []
        for i in range(1,10):
            self.board.append(i)
    def display_board(self):
        print("--------------")
        for i in range(9):
            print(f"| {self.board[i]} ",end="")
            if i == 2 or i == 5:
                print(' | ')
                print('----+----+----')
        print(' | ')
        print("--------------")

    def update_board(self,choice,symbole):
        if self.is_valid_move(choice,symbole):
            self.board[choice - 1] = symbole
            return True
        else:
            return False
    def reset_board(self):
        for i in range(1,10):
            self.board.insert(i-1,i)
    def is_valid_move(self,choice,symbole):
        return  (choice in self.board and self.board[choice-1] != symbole)
    def gain_board(self,row):
        for i in row:
            self.board.insert(i,'*')
