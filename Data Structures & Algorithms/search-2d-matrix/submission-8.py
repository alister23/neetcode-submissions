class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def convert(i):
            return [i//n, i%n]

        left = 0
        right = m*n-1

        while left <= right:
            mid = (left + right) // 2
            index = convert(mid)
            elt = matrix[index[0]][index[1]]
            if elt == target:
                return True
            elif elt < target:
                left = mid + 1
            else:
                right = mid - 1

        return False