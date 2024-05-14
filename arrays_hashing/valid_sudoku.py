'''
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
create 3 dictionaries to map the seen elements of a particular row, column, or grid.
Iterate through board, and check if the index is filled.
If so, check if the element has already been seen in the same row, col, or grid and do appropriate action.
If seen, return False else add current index, to dictionaries
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

