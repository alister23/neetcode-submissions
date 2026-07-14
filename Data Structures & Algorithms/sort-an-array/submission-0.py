class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        out = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1
        
        if i < len(left):
            out += left[i:]
        if j < len(right):
            out += right[j:]

        return out