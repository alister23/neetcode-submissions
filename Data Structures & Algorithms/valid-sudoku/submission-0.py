class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # print("rows")
        if all(self.isValidSubgroup(row) for row in board):
            columns = []
            for i in range(9):
                columns.append([row[i] for row in board])
            # print("columns")
            if all(self.isValidSubgroup(column) for column in columns):
                subboxes = []
                for i in range(3):
                    for j in range(3):
                        subbox = []
                        for x in range(3):
                            for y in range(3):
                                subbox.append(board[3*i+x][3*j+y])
                        subboxes.append(subbox)
                # print("subboxes")
                if all(self.isValidSubgroup(subbox) for subbox in subboxes):
                    return True
        return False



    def isValidSubgroup(self, nums: List[str]) -> bool:
        digits = []
        for num in nums:
            if num.isdigit():
                digits.append(nums)
        # print(digits)
        # digits_set = set(digits)
        if len(digits) == len(set(nums)-{"."}):
            return True
        # print("failed on", nums)
        return False