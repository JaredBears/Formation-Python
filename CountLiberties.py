'''
Go is an ancient game played on a board of 19x19 grid of lines. Black and white stones are placed at the intersections of these lines. A group of stones of one color is considered a _connected_ if every stone in the group is reachable from every other, traveling horizontally or vertically. For example, the following shows a is a single connected white group because we can traverse through all stones without jumps or moving diagonally. 

  0 1 2 3 4 5
0 + + W + + +
1 + + W + + +
2 + + W W + +
3 + + + W W +
4 + + + + + +
5 + + + + + +

A connected group of stones is captured when *all* adjacent points to the group are occupied by stones of the opposite color. Unoccupied intersections adjacent to a group of stones are called _liberties_. While playing the game, players must keep track of their groups and their liberty counts to look for strong moves to play.

The previous example group of white stones has 10 liberties. If the stone at (2, 3) is removed, it would be broken into two groups. The vertical group of three has 7 liberties, and the horizontal group of two has 6:

  0 1 2 3 4 5
0 + + W + + +
1 + + W + + +
2 + + W + + +
3 + + + W W +
4 + + + + + +
5 + + + + + +

Given a 19x19 board and an occupied position on the board, count the liberties of that connected group. Assume that the board is square and, at most 19x19, the size of a real Go board.
 

EXAMPLE(S)
countLiberties(
  [
    ['+', '+', '+'],
    ['+', 'W', '+'],
    ['+', '+', '+'],
  ],
  1, 1) == 4

countLiberties(
  [
    ['+', '+', '+'],
    ['+', 'B', 'B'],
    ['+', '+', 'B'],
  ],
  1, 1) == 4

Similar to the last example, but the new stone isn't connected.
countLiberties(
  [
    ['B', '+', '+'],
    ['+', 'B', 'B'],
    ['+', '+', 'B'],
  ],
  1, 1) == 4

countLiberties(
  [
    ['W', '+', 'W'],
    ['W', 'B', 'B'],
    ['W', 'W', 'B'],
  ],
  1, 1) == 1
 

FUNCTION SIGNATURE
function countLiberties(board, x, y) {

initialize a set for visited
    check up from the starting coord
        down
        left
        right
    if at any point, we run into unocuppied, increment liberties
    if at any point, we run into the same color, recurse on new point
    At each point, add to visited
'''

def countLiberties(board, x, y):
    visited = set()
    liberties = 0
    base = board[x][y]
    def dfs(x, y):
        nonlocal liberties
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            # out of bounds
            return
        if (x, y) in visited: 
            return
        visited.add((x, y))
        if board[x][y] == '+': 
            liberties += 1
            return
        if board[x][y] == base:
            dfs(x-1, y) # up
            dfs(x+1, y) # down
            dfs(x, y-1) # left
            dfs(x, y+1) # right
    dfs(x, y)
    return liberties

testOne = [
    ['+', '+', '+'],
    ['+', 'W', '+'],
    ['+', '+', '+'],
]

testTwo = [
    ['+', '+', '+'],
    ['+', 'B', 'B'],
    ['+', '+', 'B'],
]

print(countLiberties(testOne, 1, 1) == 4)
print(countLiberties(testTwo, 1, 1) == 4)