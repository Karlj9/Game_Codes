import time
from player import HumanPlayer, RandomComputerPlayer, tictactoe_Computer                             # Call the other program

class tictactoe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]                            # we make a liste of 3x3 to make a board of 9
        self.current_winner = None                                      # Don't give a winner yet

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")                        # Creat a table with | , it make 3 list of 3 
    @staticmethod                                                       # Use a static function staticmethod()

    def print_board_nums():
        number_board = [[str(i) for i in range (j*3,(j+1)*3)]for i in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")                        # Creat a table with | , it make 3 list of 3

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True                                                 # If the winner get a letter it return true
        return False                                                    # Else it return false

    def winner (self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1) * 3]
        if all([spot == letter for spot in row]):
            return True

    def play(game, x_player, o_player, print_game=True):
        if print_game:
            game.print_board_nums()
        letter = 'X'                                                    # Starting letter, first player to play
        while game.empty_square():                                      # While the player can play on the 9 squares board
            if letter == 'O':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)
            if game.make_move(square, letter):
                if print_game:
                    print(letter + f + "make a move to square {square}")
                    game.print_board()
                    print('')                                           # Return an empty line
                if game_current_winner:
                    if print_game:
                        print(letter + 'WINS!!!!')
                    return letter
                letter = 'O' if letter == 'X' else 'X'
            time.sleep(0.9)
        if print_game:
            print('TIE !!!')
    if __name__ == '__main__':
        x_player = HumanPlayer('X')
        o_player = tictactoe_Computer('X')
        game = tictactoe
        play(game, x_player, o_player, print_game=True)
    
                    
