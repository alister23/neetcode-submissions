class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        while left <= right:
            # print(left, mid, right)
            if mid == 0 and (len(nums) == 1 or nums[1] > nums[mid]): return nums[0]
            if mid < len(nums)-1 and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] < nums[0]:
                right = mid-1
            else:
                left = mid+1
            mid = (left+right)//2
        return nums[0]