from enum import Enum 

"""

**Design Tic-Tac-Toe**

- 2 players X,0
- playing a 3x3
- move(row, col)
- if cell is occupied: reject
- game end when someone wins or board is full 

Core features:
- players can make move depending on state of game
- same symbol in a row horizontally, vertically or diagonally: a match and declare the winner
- if board gets full, declare a tie



Classes:

Tic-Tac-toe
- board : 3 by 3 of empty slots
- players: X or 0
- current player
- game state

+ make_move(Player, row, col): check if valid and place side
+ check_streak(row, col):

Player:
- side

For each of the four orientations, I can traverse n cells in each director. Thats a constant number of traversals: 0(n) + 0(n) + 0(n) + 0(n) ~ 0(n)

Edges:

- if a player tries to make a move after the game has already ended: 

"""

enum class Side:
    X = "X"
    O = "0"


enum class State:
    full = "full"
    X.winner = "X.winner"
    Y.winner = "Y.winner"


class Tic-Tac-Toe:
    board: List
    def __init__(self):
        for i in range(3):
            self.board = [[.]* 3]
        self.players = [Side.X, Side.O]
    
    def make_move(self, Player, row, col):
        if 0 <= row <= 3 and 0 <= col <= 3 and board[row][col] == [.]:
            board[row][col] = Player.side
            self.check_streak(Player, row, col)
        else:
            raise ValueError

    def check_streak(self, Player, row, col):
        r = row
        c = col

        count = 0

        while r < 3:
            r += 1
            if board[r][c] == Player.Side:
                count += 1 
        
        while c < 3:
            c += 1
            if board[r][c] == Player.Side:
                count += 1 
        
        while r > 0:
            r -= 1
            if board[r][c] == Player.Side:
                count += 1 
        
        while c > 0:
            c -= 1
            if board[r][c] == Player.Side:
                count += 1 

class Player:
    def __init__(self, side):
        self.side = side
    



        