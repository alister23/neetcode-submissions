class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_rows():
            for row in board:
                seen = set()
                for char in row:
                    if char in seen and char != '.':
                        return False
                    seen.add(char)
            return True

        def check_cols():
            for col in range(len(board)):
                seen = set()
                for row in board:
                    if row[col] in seen and row[col] != '.':
                        return False
                    seen.add(row[col])
            return True

        def check_squares():
            for i in range(3):
                for j in range(3):
                    seen = set()
                    for k in range(3):
                        for l in range(3):
                            if board[i*3+k][j*3+l] in seen and board[i*3+k][j*3+l] != '.':
                                return False
                            seen.add(board[i*3+k][j*3+l])
            return True

        return check_rows() and check_cols() and check_squares()