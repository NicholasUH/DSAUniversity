class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        grids = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in grids[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                grids[(r//3), c//3].add(board[r][c])
        return True

        '''
        create hashmaps row/col/grid : set of numbers in that respective row/col/grid
        iterate thru entire board
        -if empty, skip
        -check if the current position's value has already been seen in the same row, same col, and same grid
            -return False
        add current position to hashsets
        '''