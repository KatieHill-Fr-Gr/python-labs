
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
        print("Ready to play?")
        while self.winner is None and self.tie == False:
                self.render()
                self.place_piece()
                self.check_winner()
                self.check_for_tie()
                self.switch_turn()
    
        self.render()


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
            win_conditions = [
                ['a1', 'b1', 'c1'],
                ['a2', 'b2', 'c2'],
                ['a3', 'b3', 'c3'],
                ['a1', 'a2', 'a3'],
                ['b1', 'b2', 'b3'],
                ['c1', 'c2', 'c3'],
                ['a1', 'b2', 'c3'],
                ['a3', 'b2', 'c1']
            ]
           
            for combo in win_conditions:
                if (self.board[combo[0]] and
                    self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]):
                    self.winner = self.turn
                    print(f'{self.winner} has won the game!')
                    return True
            
            return False
    
    def check_for_tie(self):
        if None not in self.board.values() and self.winner is None:
            self.tie = True
            print("It's a tie!")

    
    def switch_turn(self):
        # if self.turn == "X":
        #     self.turn = "O"
        # elif self.turn == "O":
        #     self.turn = "X"
        self.turn = {"X": "O", "O": "X"}[self.turn] 

# {"X": "O", "O": "X"} creates the dictionary
# [self.turn] immediately looks up whatever value self.turn contains


tic_tac_toe = Game()
tic_tac_toe.play_game()




