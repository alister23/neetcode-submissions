class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        mid = (left+right)//2
        row = -1
        while left <= right:
            # print(left, right, mid)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                if mid == len(matrix)-1:
                    row = len(matrix)-1
                    break
                elif matrix[mid+1][0] == target:
                    return True
                elif matrix[mid+1][0] > target:
                    row = mid
                    break
                elif matrix[mid+1][0] < target and mid+1 == len(matrix)-1:
                    row = mid+1
                    break
                else:
                    left = mid+1
            elif matrix[mid][0] > target:
                right = mid-1
            mid = (left+right)//2
        if row == -1: return False
        print("row found", row)
        left = 0
        right = len(matrix[row])-1
        mid = (left+right)//2
        while left <= right:
            print(left, right, mid)
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                right = mid-1
            else:
                left = mid+1
            mid = (left+right)//2
        return False

