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





