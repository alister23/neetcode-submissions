class Solution:
    def checkRow(numbers):
        appeared = set()
        for num in numbers:
            if num in appeared:
                return False
            if num not in '123456789.':
                return False
            if num != '.':
                appeared.add(num)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not all(Solution.checkRow(row) for row in board):
            return False
        if not all(Solution.checkRow([row[i] for row in board]) for i in range(len(board))):
            return False
        if not all(Solution.checkRow([board[i*3+x][j*3+y] for x in [0,1,2] for y in [0,1,2]]) for i in [0,1,2] for j in [0,1,2]):
            return False
        return True
        