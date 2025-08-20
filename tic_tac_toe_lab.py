
class Game():
    def __init__(self, turn='X', tie=False, winner=None):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print("Welcome to the game. Enter a square to make your first move")

    def print_board(self):
        b = self.board
        print(f"""
             A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
          """)
        
    def print_message(self):
        if (self.tie==True):
            print('Tie game!')
        elif (self.winner != None):
            print(f'{self.winner} wins the game!')
        else:
            print(f"It is player {self.turn}'s turn")

    def render(self):
        self.print_board()
        self.print_message()

    def place_piece(self):
        while True:
            move = input(f"Enter the square you want to place your piece in (example: A1): ").lower()
            if move in self.board and self.board[move] == None:
                self.board[move] = self.turn
                break
            else: 
                print("Invalid move. Please try again")

    def check_winner(self):
        self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1'])
        self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2'])










tic_tac_toe = Game()
tic_tac_toe.play_game()




