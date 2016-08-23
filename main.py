import math
import random

class tick_tac_toe:

    grid_size = 3

    # board = [" ", " ", " ",
    #          " ", " ", " ",
    #          " ", " ", " ", ]

    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    # winning_combinations = [[0, 1, 2],
    #                         [3, 4, 5],
    #                         [6, 7, 8],#
    #                         [0, 3, 6],#
    #                         [1, 4, 7],#
    #                         [2, 5, 8],#
    #                         [0, 4, 8],
    #                         [2, 4, 6]]
    winning_combinations = [
        [[0,0], [0,1], [0,2]],
        [[1,0], [1,1], [1,2]],
        [[2,0], [2,1], [2,2]],
        [[0,0], [1,0], [2,0]],
        [[0,1], [1,1], [2,1]],
        [[0,2], [1,2], [2,2]],
        [[0,0], [1,1], [2,2]],
        [[0,2], [1,1], [2,0]]
    ]

    # Player Name, Symbol, Turn
    players = [["Player One", "O", True], ["Player Two", "X", False]]

    def __init__(self):
        print("Tic Tac Toe!!!")

    def edit_name(self):
        pass

    def occupied(self, position):
        x = position[0]
        y = position[1]
        if self.board[x][y] == " ":
            return False
        else:
            return True

    def swap_turns(self):
        if self.players[0][2]:
            self.players[0][2] = False
            self.players[1][2] = True

        else:
            self.players[0][2] = True
            self.players[1][2] = False

    def update_board(self, position, player):
        msg = "You can't over lap the other players pieces! Try Again"
        if self.occupied(position):
            return msg
            self.game()
        else:
            x = position[0]
            y = position[1]
            self.board[x][y] = self.players[player][1]

    def show_board(self):
        print("/-----------------\\ \n"
              "|  {0}  |  {1}  |  {2}  |\n"
              "|-----------------|\n"
              "|  {3}  |  {4}  |  {5}  |\n"
              "|-----------------|\n"
              "|  {6}  |  {7}  |  {8}  |\n"
              "\-----------------/".format(self.board[0][0], self.board[0][1], self.board[0][2],
                                           self.board[1][0], self.board[1][1], self.board[1][2],
                                           self.board[2][0], self.board[2][1], self.board[2][2]))

    def tutorial(self):
        pass

    def AI(self):
        pass

    @property
    def winner(self):
        for player in range(0, 1):
            for winning_combo in range(0,7):
                x1 = self.winning_combinations[winning_combo][0][0]
                y1 = self.winning_combinations[winning_combo][0][1]
                x2 = self.winning_combinations[winning_combo][1][0]
                y2 = self.winning_combinations[winning_combo][1][1]
                x3 = self.winning_combinations[winning_combo][2][0]
                y3 = self.winning_combinations[winning_combo][2][1]

                if self.players[player][1] in self.board[x1][y1]:
                    if self.players[player][1] in self.board[x2][y2]:
                        if self.players[player][1] in self.board[x3][y3]:
                            return True

            return False

    def game(self):
        while not self.winner:
            if self.players[0][2]: # If player one's turn
               player = 0
            else: # If player two's turn
                player = 1

            print("Player {0}'s turn!".format(self.players[player][0]))

            play = []

            x = int(input("Input the x-cord of your move: "))
            y = int(input("Input the y-cord of your move: "))

            try:
                play.append(x)
                play.append(y)
            except:
                print("Fill in both values!!!")
                self.game()

            self.update_board(play, player)
            self.show_board()

            self.swap_turns()

        print("winner!!!")

if __name__ == '__main__':
    tick_tac_toe = tick_tac_toe()
    tick_tac_toe.game()
