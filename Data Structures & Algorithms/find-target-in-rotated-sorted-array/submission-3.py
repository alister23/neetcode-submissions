class Solution:
    def findBreak(nums):
        left = 0
        right = len(nums)-1
        mid = (left+right)//2

        while left <= right:
            if mid == len(nums)-1:
                return mid
            if nums[mid] > nums[mid+1]:
                return mid
            if nums[mid] >= nums[0]:
                left = mid+1
            else:
                right = mid-1
            mid = (left+right)//2


    def search(self, nums: List[int], target: int) -> int:
        join = Solution.findBreak(nums)
        if nums[0] <= target <= nums[join]:
            left = 0
            right = join
        else:
            left = join+1
            right = len(nums)-1
        mid = (left+right)//2
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
            mid = (left+right)//2
        return -1