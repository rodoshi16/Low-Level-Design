from enum import Enum 

"""

**Design Tic-Tac-Toe**

- 2 players X,0
- playing a 3x3
- players can make a move(row, col)
- if cell is occupied: reject
- game end when someone wins or board is full 

Core features:
- players can make move depending on state of game
- same symbol in a row horizontally, vertically or diagonally: a match and declare the winner
- if board gets full, declare a tie



classes:

class Player(Enum):
    X = "X"
    0 = "0"

class State(Enum):
    END = "THE GAME IS OVER"
    FULL = "THE BOARD IS FULL, ITS A DRAW"
    X.WINNER = "X IS THE WINNER"
    Y.WINNER = "Y IS THE WINNER"


class Tic-Tac-Toe:
    - self.spots: [.] *3
    - self.players: enum class (of X or 0)
    - self.occupied: 0 

    + make_move(Player, row, col): in this class because player doesnt have internal details of the board

    check if row, col is invalid and if not empty - raise error
    and the state is not ended then place a move and check for streak
    if streak, end the game and display the winner, set state of game to end
    if no streak, check if 9-self.occupied == 0, change state to full and return msg


    + check_streak(self, row, col): check horizontal, vertical to see if theres a count of least 3 in one direction
   

class Player:
    - side: enum class


"""

class Side(Enum):
    X = "X"
    O = "0"

class State(Enum):
    END = "THE GAME IS OVER"
    EMPTY = "THE BOARD IS EMPTY"
    FULL = "THE BOARD IS FULL, ITS A DRAW"

class Tic-Tac-Toe:
    self.spots: List
    def __init__(self):
        self.spots = []
        for i in range(3):
            self.spots.append([.] * 3)
        self.players = [X, O]
        self.occupied = 0 
    self.State = State.EMPTY
    
    def make_move(self, Player, row, col) -> Optional[Str]:
        if 0 <= row <= 3 and 0 <= col <= 3 and self.State != State.END and self.State != State.FULL and self.spots[row][col] == [.]:
            self.spots[row][col] = Player.Side
            if check_streak(self, row, col, Player):
                self.State = END
                return f'{Player.Side} is the Winner!!!'
            else:
                return None

        else:
            raise ValueError
    
    def check_streak(self, row, col, Player):
        #check for diagonals
        count = 0
        while row <= 3:
            if self.spots[row][col] == Player.Side:
                count += 1
            row += 1

        while row >= 0:
            if self.spots[row][col] == Player.Side:
                count += 1
            row -= 1 

        if count == 3:
            return True
        
        count = 0
        
        while col <= 3:
            if self.spots[row][col] == Player.Side:
                count += 1
            count += 1

        
        while col >= 0:
            if self.spots[row][col] == Player.Side:
                count += 1
            col -= 1
        
        if count == 3:
            return True

class Player:
    def __init__(self, side):
        self.Side = side

        

