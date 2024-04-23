# !/usr/bin/env python3
import random
import time


class TicTacToe3D:
    def __init__(self):

        self.board = []
        # Initialize 3D board with None
        for _ in range(3):
            depth = []
            for _ in range(3):
                row = []
                for _ in range(3):
                    row.append(None)
                depth.append(row)
            self.board.append(depth)

        self.players = []
        self.current_player = None
        # Players[0] get the X symbol , Players[1] get the O symbol
        self.symbols = ['X', 'O']
        self.scores = []
        


    
    def print_board(self):
     for depth in range(3):
        print("\nDepth", depth + 1)
        for row in range(3):
            # Print the cells of the row
            for column in range(3):
                if self.board[row][column][depth]:
                    print(self.board[row][column][depth], end='')
                else:
                    print(' ', end='')
                # Print separator between columns 
                if column < 2:
                    print(' | ', end='')
            # Print separator between rows
            if row < 2:
                print("\n---------")
            else:
                print()  #print Enter between Depths
    


    def is_valid_move(self, move):
        row, column, depth = move
        return 0 <= row < 3 and 0 <= column < 3 and 0 <= depth < 3 and self.board[row][column][depth] is None

    
      
    def get_move(self):
        while True:
            try:
                move = input("Enter your move (row, column, depth): ")
                move = tuple(map(int, move.split(',')))
                if self.is_valid_move(move):
                    return move
                else:
                    print("Invalid move, Please try again.")
            except ValueError:
                print("Invalid input, Please enter three integers separated by commas.")



    def make_move(self, move):
        row, column, depth = move
        self.board[row][column][depth] = self.symbols[self.players.index(self.current_player)]

        

    def check_win(self):           
        # Check rows 
        for i in range(3):
            for j in range(3):
                if self.board[i][0][j] == self.board[i][1][j] == self.board[i][2][j] != None:
                    return True
     
        # Check rows (depth)
        for i in range(3):
                if self.board[i][0][0] == self.board[i][1][1] == self.board[i][2][2] != None:
                    return True
        
        # Check columns
        for i in range(3):
            for j in range(3):
                if self.board[0][i][j] == self.board[1][i][j] == self.board[2][i][j] != None:
                    return True
           
        # Check columns (depth)
        for j in range(3):
                if self.board[0][j][0] == self.board[1][j][1] == self.board[2][j][2] != None:
                    return True 
         
        # Check diagonals
        for i in range(3):
                # Check first diagonal
                if self.board[0][0][i] == self.board[1][1][i]== self.board[2][2][i] != None:
                    return True

                # Check secondary diagonal
                if self.board[0][2][i] == self.board[1][1][i] == self.board[2][0][i] != None:
                    return True

        # Check diagonals (depth)
        if self.board[0][0][0] == self.board[1][1][1] == self.board[2][2][2] != None:
            return True
        if self.board[0][2][0] == self.board[1][1][1] == self.board[2][0][2] != None:
            return True
        
        # Check vertical  
        for i in range(3):
            for j in range(3):
                if self.board[i][j][0] == self.board[i][j][1] == self.board[i][j][2] != None:
                   return True
        

   
    def check_tie(self):
        for depth in range(3):
          for row in range(3):
            for column in range(3):
                 if self.board[row][column][depth] is None:
                     return False
        return True
    


    def switch_player(self):
        self.current_player = self.players[(self.players.index(self.current_player) + 1) % 2]
    
   

    def play_again(self):
        while True:
            choice = input("Do you want to play again? (yes/no): ").lower()
            if choice in ['yes', 'y']:
                return True
            elif choice in ['no', 'n']:
                return False
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")



    def reset_board(self):
        self.board = [[[None] * 3 for _ in range(3)] for _ in range(3)]



    def start_game(self):
        print("Welcome to 3-D triple-decker tic-tac-toe game ^_^")
        self.players.append(input("Enter the first player name: "))
        self.players.append(input("Enter the second player name: "))
        self.current_player = random.choice(self.players)
        # Initialize scores to 0 for each player
        for player in self.players:
          self.scores.append(0)
        
        while True:
           print(f"\n{self.current_player}'s turn:")
           self.print_board()  
           move = self.get_move() 
           self.make_move(move)
           if self.check_win():
               self.print_board()
               print(f"\nCongratulations, {self.current_player} wins!")
               self.scores[self.players.index(self.current_player)] += 1  # Update player's score
               print("Scores:")
               for player in self.players:
                    print(f"{player}: {self.scores[self.players.index(player)]}")
               if self.play_again():
                    self.reset_board()
               else:
                 print("\nGood Bye")
                 break           
           elif self.check_tie():
                 self.print_board()
                 print("\nIt's a tie!")
                 if self.play_again():
                    self.reset_board()
                 else:
                    print("\nGood Bye")
                    break
           self.switch_player()
            
            
game = TicTacToe3D()
game.start_game()

