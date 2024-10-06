class Menu:
    def display_main_menu(self):
        print("welcome to the X-O GAME ")
        print("1. start game")
        print("2. quit game")
        choice = int(input("enter your choice: "))
        while choice !=1 and choice != 2:
            choice = int(input("error enter 1 or 2: "))
        return choice
    def display_endGame_menu(self):
        menu_text = """"
        Game over!
        1.restart the game
        2.quit the game
        enter your choice
        """
        choice = int(input(menu_text))
        while choice !=1 or choice != 2:
            choice = int(input("error enter 1 or 2: "))
        return choice
