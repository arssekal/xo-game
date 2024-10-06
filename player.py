class Player:
    def __init__(self):
        self.name = ""
        self.symbole = ""
    def chose_name(self):
        while True:
            name = input("enter your name: ")
            if name.isalpha():
                self.name = name
                break
            else:
                print("/!\ error only letters accepted")
    def choose_symbole(self):
        while True:
            symbole = input(f"{self.name}, choose your symbole letter: ").upper()
            if symbole.isalpha() and len(symbole) == 1:
                self.symbole = symbole
                break 
            else:
                print("/!\ make sure you type 1 aphabet")