class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m-1
        mid = (left+right)//2
        while left <= right:
            print("searching row", mid)
            if matrix[mid][0] < target:
                left = mid+1
            elif matrix[mid][0] > target:
                right = mid-1
            else:
                print("found at first elt of row", mid)
                return True
            mid = (left+right)//2
        if left >= m or matrix[left][0] > target:
            left -= 1
        print("found row", left)
        row = matrix[left]
        left = 0
        right = n-1
        mid = (left+right)//2
        while left <= right:
            print('searching index', mid, 'of row')
            if row[mid] < target:
                left = mid+1
            elif row[mid] > target:
                right = mid-1
            else:
                print('found')
                return True
            mid = (left+right)//2
        return False

