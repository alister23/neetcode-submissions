class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        middle = (right+left)//2
        while left <= right:
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle-1
                middle = (right+left)//2
            elif nums[middle] < target:
                left = middle+1
                middle = (right+left)//2
            # if left >= right-1:
            #     if nums[left] != target and nums[right] != target:
            #         break
        return -1