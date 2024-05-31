'''
Problem:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

'''
Logic:
The logic behind this problem seeing if the board is valid based on the rules of sudoku. The idea behind the solution is to iterate through 
the board and check if the number has already been seen in the row, column, and grid and return the appropriate answer. To check if the number
is valid, we can create three dictionaries that maps the (row, column, grid) to a set that will contain the numbers seen in the row, column, and grid.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grids = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] is not ".":
                    if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grids[(r // 3, c // 3)]:
                        return False
                    
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    grids[(r//3 , c//3)].add(board[r][c])
        
        return True

