class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell == '.':
                    continue

                row_cell = (cell, 'row', row)
                col_cell = (cell, 'col', col)
                box_cell = (cell, 'box', ((row//3)*3) + col//3)

                if row_cell in seen or col_cell in seen or box_cell in seen:
                    return False
                
                seen.add(row_cell)
                seen.add(col_cell)
                seen.add(box_cell)

        return True