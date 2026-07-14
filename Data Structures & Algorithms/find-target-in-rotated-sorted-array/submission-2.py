class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minimum = -1
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        while left <= right:
            # print(left, mid, right)
            if mid == 0 and (len(nums) == 1 or nums[1] > nums[mid]):
                minimum = 0
                break
            if mid < len(nums)-1 and nums[mid] > nums[mid+1]:
                minimum = mid+1
                break
            elif nums[mid] < nums[mid-1]:
                minimum = mid
                break
            elif nums[mid] < nums[0]:
                right = mid-1
            else:
                left = mid+1
            mid = (left+right)//2
        if minimum == -1:
            minimum = 0
        print("minimum found", minimum)
        if minimum == 0:
            left = 0
            right = len(nums)-1
        else:
            if target >= nums[0]:
                left = 0
                right = minimum-1
            else:
                left = minimum
                right = len(nums)-1
        mid = (left+right)//2
        for _ in range(4):
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
            mid = (left+right)//2
        return -1