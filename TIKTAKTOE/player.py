#=============================================| Tic-tac-toe  with an AI |===============================================#
        #   +=====+=====+=====+
        #   |  O  |  X  |  O  |
        #   +=====+=====+=====+
        #   |  X  |  O  |  X  |
        #   +=====+=====+=====+
        #   |  X  |  X  |  O  |
        #   +=====+=====+=====+
# We are going to do a tic-tac-toe game  with Python
import math
import random

#==================================================| Class Player |=====================================================# 
class Player:
    def __init__(self, letter):                                         # We make a function called __init__   | the player have to put information
        self.letter = letter                                            # Set a letter X or O

    def get_move (self, game):
        pass
#===========================================| Class Random Coputer Player |============================================# 
class RandomComputerPlayer(Player):
    def __init__(self, letter):                                         # We make a function called __init__   | the player have to put information
        super().__init__(letter)                                        # Iniotialization of a Parent class, which is letter

    def get_move (self, game):
        square = random.choice(game.available_moves())

#===============================================| Class HumanPlayer |==================================================# 
class HumanPlayer(Player):
    def __init__(self, letter):                                         # We make a function called __init__   | the player have to put information
        super().__init__(letter)                                        # Iniotialization of a Parent class, which is letter

    def get_move (self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input love (0-9):')
            try:
                val = int(square)
                if val not in game.invailable_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
    

#=============================================| Class TicTacToe Coputer |==============================================# 
class tictactoe_Computer (Player):                                      # We make a class in with we are going to make the game
    def __init__(self, letter):                                         # We make a function called __init__   | the player have to put information
        super().__init__(letter)                                        # Iniotialization of a Parent class, which is letter
        
    def get_move(self, game):                                           # We get the self information
        if len(game.available_moves()) == 9:                            # We set the number of squares in the game at 9
            square = random.choice(game.available_moves())              # Choose ramdomly a 'square' in the table
        else :
            square = self.minimax(game, self.letter)['position']        # Use minimax and letter as methods on the 'self' instance
        return square
    def minimax(self, state, Player):
        max_player = self.letter                                        # The 'main player' 
        other_player = 'O' if player == 'X' else 'X'                    # Changing player, one with 'O' the other with 'X', moving between each other
        if state.current_winner == other_player:
            # give the winner position for the score
            return {'posithion' : None,
                    'score' : 1 * (state.num_empty_square() + 1 ) if other_player == max_player else -1 * (state.num_empty_square() + 1 )
                    }
        elif not state.num_empty_square():                              # If there is no empty squares
            return {'posithion' : None,
                    'score' : 0
                    }
        if Player == max_player:
            best = {'posithion' : None,                                 # Creat a 'best' dictionary
                    'score' : -math.inf                                 # Make the score biger than the max if the main player win first
                    }
        else :
            best = {'posithion' : None,                                 # Creat a 'best' dictionary
                    'score' : math.inf                                  # The score should minimize 
                    }
        for possible_move in state.avilable_moves():
            # 1 - try a spot
            state.make_move(possible_move, Player)
            # 2 - recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)               # moving to another player
            # 3 - undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            # 4 - change if necessary
            if Player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score                                    # replace the 'best' dictionary by 'sim_score' dictionary
            else :
                if sim_score['score'] < best['score']:
                    best = sim_score                                    # replace the 'best' dictionary by 'sim_score' dictionary
        return best
        
