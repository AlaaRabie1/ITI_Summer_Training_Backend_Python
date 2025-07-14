# 1. run the app
# 2. main menu
# 3. start game, quit game
# 4. player1 name, symbol (x,o), player2 name,symbol
# 5. board is displayed
# 6. game loops until win or draw
# 7. another menu: restart game, quit game

# class for: player, board, menu, game 
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""


    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha() == True:
                self.name = name
                break
            print("Invalid name, Please use letters only.")


    def choose_symbol(self, other):
        while True:
            symbol = input(f"{self.name}, Enter your symbol (one letter only): ")
            if symbol.isalpha() and len(symbol) == 1:
                if symbol != other.symbol:
                    self.symbol = symbol
                    break
                else:
                    print("This symbol already in use, choose another one.")
            else:
                print("Invalid symbol, Please choose one letter.")


class Menu:
    # dont need init cause we dont have attributes
    def validate_choice(self, choice):
        if choice != '1' and choice != '2':
            return False
        else: 
            return True
        

    def display_main_menu(self):
        print("Welcome to my X-O game!")
        while True:
            print("1. Start Game")
            print("2. Quit Game")
            choice = input("Enter your choice (1 or 2): ")
            if self.validate_choice(choice):
                return choice
            else:
                print("Please enter (1 or 2)")
            
        
    def display_endgame_menu(self):
        menu_text = '''
Game Over!
1. Restart Game 
2. Quit Game
Enter your choice (1 or 2): '''
        while True:
            choice = input(menu_text)
            if self.validate_choice(choice):
                return choice
            else:
                print("Please enter (1 or 2)")
    

class Board:
    def __init__(self):
        self.board = [ str(i) for i in range(1,10) ] # [ "1" , "2" , "3" , ....]


    def display_board(self):
        for i in range(0,len(self.board),3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-"*5)


    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        return False
    

    # solid principles, single responsibility principle 
    def is_valid_move(self, choice):
        return self.board[choice-1].isdigit()


    def reset_board(self):
        self.board = [ str(i) for i in range(1,10) ] 


class Game:
    def __init__(self):
        # all objects should be defined inside out game class cant be outside
        self.board = Board()
        self.players = [Player(), Player()]
        self.menu = Menu()
        self.cur_player_index = 0


    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()


    def play_turn(self):
        player = self.players[self.cur_player_index] # players[0]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9):  "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move, Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
        clear_screen()
        self.switch_player()


    def switch_player(self):
        self.cur_player_index = 1 - self.cur_player_index


    def check_win(self):
        wining_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
            [0, 4, 8], [2, 4, 6]             # diagonals

        ]

        for combo in wining_combinations:
            if(self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return True
        return False


    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)  # generator expression

 
    def restart_game(self):
        self.board.reset_board()
        self.cur_player_index = 0


    def setup_players(self):
        for number, player in enumerate(self.players):
            print(f"Player {number+1}, Enter your details: ")
            player.choose_name()
            other = self.players[1-number]
            player.choose_symbol(other)
            clear_screen()


    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win():
                clear_screen()
                self.board.display_board()
                winner = self.players[1 - self.cur_player_index]  # the player who just played
                print(f"🎉 {winner.name} wins!")
                if not self.handle_endgame():
                    break

            elif self.check_draw():
                clear_screen()
                self.board.display_board()
                print("🤝 It's a draw!")
                if not self.handle_endgame():
                    break
    

    def handle_endgame(self):
            choice = self.menu.display_endgame_menu()
            if choice == '1':
                self.restart_game()
                return True
            else:
                self.quit_game()
                return False


    def quit_game(self):
        print("Thank you for playing :)!")

G = Game()
G.start_game()
